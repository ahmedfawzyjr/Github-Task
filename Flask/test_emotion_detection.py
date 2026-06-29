import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    @patch('requests.post')
    def test_emotion_detector(self, mock_post):
        # Define mock responses based on input text
        def mock_post_side_effect(url, json=None, headers=None, timeout=None):
            text = json['raw_document']['text']
            mock_res = Mock()
            mock_res.status_code = 200
            
            # Setup emotional scores based on the input text
            emotions = {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0
            }
            
            if "glad" in text:
                emotions['joy'] = 0.9
            elif "mad" in text:
                emotions['anger'] = 0.9
            elif "disgusted" in text:
                emotions['disgust'] = 0.9
            elif "sad" in text:
                emotions['sadness'] = 0.9
            elif "afraid" in text:
                emotions['fear'] = 0.9
                
            mock_res.json.return_value = {
                'emotionPredictions': [{
                    'emotion': emotions
                }]
            }
            return mock_res
            
        mock_post.side_effect = mock_post_side_effect

        # Test joy
        res_joy = emotion_detector("I am glad this happened")
        self.assertEqual(res_joy['dominant_emotion'], 'joy')

        # Test anger
        res_anger = emotion_detector("I am really mad about this")
        self.assertEqual(res_anger['dominant_emotion'], 'anger')

        # Test disgust
        res_disgust = emotion_detector("I feel disgusted hearing about this")
        self.assertEqual(res_disgust['dominant_emotion'], 'disgust')

        # Test sadness
        res_sad = emotion_detector("I am sad about this")
        self.assertEqual(res_sad['dominant_emotion'], 'sadness')

        # Test fear
        res_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
