#pip install youtube-comment-downloader


    import csv
    from itertools import islice
    from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_RECENT


    def download_youtube_comments(video_url, limit= None, output_filename="youtube_comments.csv"):
        downloader = YoutubeCommentDownloader()

        print("댓글 수집을 시작합니다...")
        # 댓글 생성기 가져오기
        comments = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_RECENT)

        # CSV 파일로 저장 (한글 깨짐 방지를 위해 utf-8-sig 사용)
        with open(output_filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            # 헤더(컬럼명) 작성
            writer.writerow(['작성자', '댓글 내용', '좋아요 수', '작성 시점'])

            count = 0
            # 지정한 limit 개수만큼만 수집 (limit=None으로 두면 전체 수집)
            for comment in islice(comments, limit):
                writer.writerow([
                    comment['author'],
                    comment['text'],
                    comment['votes'],
                    comment['time']
                ])
                count += 1

        print(f"총 {count}개의 댓글이 '{output_filename}' 파일로 저장되었습니다!")


    # 실행하기 (원하는 URL과 수집할 댓글 개수 지정)
    video_url = "https://youtu.be/Bv4R0yucb2Q?si=BhrKHM3TI7YsiNkk"
    download_youtube_comments(video_url, limit=None, output_filename="comments.csv")