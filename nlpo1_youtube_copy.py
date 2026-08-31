import re
from collections import Counter

import googleapiclient
import googleapiclient.discovery
API_KEY='비공개'
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

#crawling comments
def get_video_comments(video_id):
    comments = []
    results = youtube.commentThreads().list(part='snippet',
                                             videoId=video_id, textFormat='plainText').execute()
    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        if 'nextPageToken' in results:
            results = youtube.commentThreads().list(part='snippet',
                                             videoId=video_id, textFormat='plainText',
                                             pageToken=results['nextPageToken']).execute()
        else:
            break
    return comments


comments = get_video_comments('원하는 동영상 아이디')
for comment in comments:
    print(comment)

from wordcloud import WordCloud
comment_text = ' '.join(comments)
word_cnt = Counter(comment_text.split())
cloud = WordCloud(width=600, font_path='C:/Windows/Fonts/malgun.ttf', background_color='white',
                  height=600).generate_from_frequencies(word_cnt)
cloud.to_file('test.png')