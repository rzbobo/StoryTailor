import openai
import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from gtts import gTTS
from bson import ObjectId  # ObjectId를 다루기 위해 필요



# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__, static_folder='static')  # 정적 폴더 설정
CORS(app)  # Enable CORS for cross-origin requests

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017")
db = client.storytailor
stories_collection = db.stories 

@app.route('/generate-story', methods=['POST'])
def generate_story():
    """
    Generate a story based on a user-provided keyword.
    """
    data = request.get_json()
    keyword = data.get('keyword', 'default keyword')

    try:
        # OpenAI ChatCompletion API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 한국어로 이야기를 만드는 스토리텔링 어시스턴트입니다."},
                {"role": "user", "content": f"'{keyword}'에 대한 이야기를 만들어주세요."}
            ]
        )
        # Extract the generated story
        story = response['choices'][0]['message']['content']
        return jsonify({"story": story})
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500

@app.route('/save-story', methods=['POST'])
def save_story():
    """
    Save the story to the database, without returning the _id field.
    """
    data = request.get_json()
    story = data.get('story')
    keyword = data.get('keyword')

    if story and keyword:
        try:
            # 데이터 저장
            saved_story = {"keyword": keyword, "story": story}
            stories_collection.insert_one(saved_story)
            return jsonify({"message": "Story saved successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Invalid data"}), 400

@app.route('/get-stories', methods=['GET'])
def get_stories():
    """
    Retrieve all saved stories from the database.
    """
    try:    
        stories = list(stories_collection.find({}, {"_id": 0}))  # "_id" 제외하고 모든 스토리 가져오기
        return jsonify({"stories": stories}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-story/<story_id>', methods=['GET'])
def get_story(story_id):
    """
    Retrieve a specific story by its ID, excluding the _id field.
    """
    try:
        story = stories_collection.find_one({"_id": ObjectId(story_id)}, {"_id": 0})
        if story:
            return jsonify(story), 200
        else:
            return jsonify({"error": "Story not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/update-story', methods=['POST'])
def update_story():
    """
    Update a story based on its keyword.
    """
    try:
        data = request.json
        keyword = data.get("keyword")
        new_keyword = data.get("newKeyword")

        if not keyword or not new_keyword:
            return jsonify({"error": "Both current keyword and new keyword are required"}), 400

        # MongoDB에서 keyword로 스토리 검색
        story = stories_collection.find_one({"keyword": keyword})
        if not story:
            return jsonify({"error": "Story not found"}), 404

        # 기존 스토리 가져오기
        existing_story = story.get("story", "")

        # GPT로 새로운 스토리 생성
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 창의적인 스토리텔링 어시스턴트입니다. 사용자가 제공한 키워드를 바탕으로 기존 이야기를 확장하고 개선하세요."},
                {"role": "user", "content": f"기존 스토리: {existing_story}\n추가 키워드: {new_keyword}\n이 이야기를 기반으로 새롭게 확장된 이야기를 작성해주세요."}
            ]
        )
        updated_story_content = response['choices'][0]['message']['content']

        # MongoDB 업데이트
        stories_collection.update_one(
            {"keyword": keyword},
            {"$set": {"story": updated_story_content}}
        )

        # 수정된 스토리를 반환
        updated_story = stories_collection.find_one({"keyword": keyword}, {"_id": 0})
        return jsonify({"updatedStory": updated_story}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/convert-to-audio', methods=['POST'])
def convert_to_audio():
    data = request.get_json()
    story = data.get('story')

    if not story:
        return jsonify({"error": "No story provided"}), 400

    try:
        # 고유 파일 이름 생성
        unique_id = uuid.uuid4().hex
        audio_file = f"static/story_audio_{unique_id}.mp3"

        # TTS 변환 및 저장
        tts = gTTS(text=story, lang='ko')
        tts.save(audio_file)

        # 오디오 파일 URL 반환
        audio_url = f"http://127.0.0.1:5000/{audio_file}"
        return jsonify({"audio_url": audio_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    """
    Basic health check endpoint.
    """
    return "Welcome to StoryTailor API!"

if __name__ == '__main__':
    app.run(debug=True)
