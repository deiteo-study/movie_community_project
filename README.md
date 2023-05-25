## 1학기 관통PJT
### (이성민, 송지윤)
---
### 📍 서비스 명

- 데이터 분석을 활용한 영화 추천 커뮤니티 서비스

---

### 프로젝트 소개

- 영화 관람에 영향을 미칠 수 있는 리뷰 데이터를 활용해 보다 나은 영화 선택을 할 수 있는 서비스 구현
- 관람객 리뷰를 기반으로 한 데이터 분석
- 유사한 영화를 추천할 수 있는 유사도 알고리즘 개발
- 리뷰 키워드 워드클라우드를 통해 한눈에 볼 수 있는 리뷰 환경 제공
- 영화추천에 도움될만한 지표

---

### 팀원 정보 및 업무 분담 내역

- 공통
    - DB 설계 및 구조 작성
    - 구현 서비스 기획 및 구체화
    - 역할을 별개로 분리하지 않고 django와 vue 동시에 진행
        
        
        |  | 역할 | 내용 |
        | --- | --- | --- |
        | 이성민(팀장) | BE  | 데이터 크롤링 및 분석 담당, 알고리즘 구현, Djano-Vue통신, django 모델 관리 |
        | 송지윤(팀원) | FE | 데이터 전처리, 서비스 UI/UX 기초 디자인, CSS, Djano-Vue통신, 자료조사 |

> 개발 환경
> 
> - `Python 3.9.x`
> - `Django 3.2.x`
> - `Vue 2`

> 사용 아키텍쳐
> 
> - `Django REST Framework` & `Vue`

---

### 목표 서비스 구현 및 실제 구현 정도

1. 목표
    - 크롤링을 통한 영화 리뷰 데이터 수집
    - 크롤링 리뷰데이터 기반 워드클라우딩
    - 리뷰 데이터 긍정/부정 분석
    - TF-IDF 알고리즘 기반 영화 추천 및 추천 알고리즘 생성
    - 커뮤니티 서비스 구현
2. 실제 구현
    - 왓차피디아 사이트 영화 리뷰 데이터 크롤링
    - 크롤링 리뷰 데이터 및 영화 제목 키워드 유사도 비교를 위한 머신러닝(코사인 유사도)
    - 사용자 리뷰를 반영한 실시간 워드클라우딩 기능 생성
    - 영화별 관련 영화 추천 기능
    - 키워드 기반 영화 검색 기능
    - 커뮤니티 내 리뷰와 리뷰 댓글 서비스 생성

---

### 프로젝트 규칙

| Type 키워드 | 사용 시점 |
| --- | --- |
| 첫 커밋 | CREATE: start project |
| feat | 새로운 기능 추가 |
| fix | 버그 수정 |
| docs | 문서 수정 |
| style | 코드 스타일 변경 (코드 포매팅, 세미콜론 누락 등)기능 수정이 없는 경우 |
| design | 사용자 UI 디자인 변경 (CSS 등) |
| test | 테스트 코드, 리팩토링 테스트 코드 추가 |
| refactor | 코드 리팩토링 |
| build | 빌드 파일 수정 |
| ci | CI 설정 파일 수정 |
| perf | 성능 개선 |
| chore | 빌드 업무 수정, 패키지 매니저 수정 (gitignore 수정 등) |
| rename | 파일 혹은 폴더명을 수정만 한 경우 |
| remove | 파일을 삭제만 한 경우 |
| readme | README |
| comment | 주석관련 |
- ***commit message***
    - commit은 최대한 자세히

`키워드(대문자) :  (영어로 위치/함수/기능) + 한국말 설명`

---

### 데이터베이스 모델링(ERD)

![asdf.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9648c0a7-6972-4467-a55c-b6f0b838d823/asdf.png)

---

### API 설계

- server
    
    
    | HTTP verb | URL 패턴 | 설명 |
    | --- | --- | --- |
    |  | admin/ | admin.site.urls |
    |  | api/v1/ | include('movies.urls') |
    |  | accounts/ | include('accounts.urls') |
- accounts
    
    
    | HTTP verb | URL 패턴 | 설명 |
    | --- | --- | --- |
    |  | accounts/ | include('dj_rest_auth.urls') |
    | POST | accounts/signup/ | include(’dj_rest_auth.registration.urls’)(회원가입) |
    | POST | accounts/login/ | include('dj_rest_auth.urls')(로그인) |
    | POST | accounts/logout/ | include('dj_rest_auth.urls')(로그아웃) |
    | POST | accounts/ password/change/ | include('dj_rest_auth.urls')(비밀번호 변경) |
    | GET | accounts/alluser/ | 모든 유저 데이터 조회 |
    | GET | accounts/<int:userId>/get_name/ | 유저 이름 조회 |
    | GET | accounts/<str:username>/get_user/ | 유저 정보 조회 |
    | GET | accounts/delete/ | 회원탈퇴 |
    | POST | accounts/<int:userId>/follow/ | 유저 follow 기능 |
- movies
    
    
    | HTTP verb | URL 패턴 | 설명 |
    | --- | --- | --- |
    | GET | api/v1/<int:movieId>/get_movie/ | 영화 정보 조회 |
    | GET | api/v1/random/ | 랜덤 영화, 장르 조회 |
    | GET | api/v1/recommendmovies/ | 사용자 별 추천 영화 조회 |
    | GET | api/v1/<int:movieId>/get_reviews/ | 영화의  모든 리뷰 조회 |
    | GET | api/v1/<int:reviewId>/get_review/ | 해당 리뷰 조회 |
    | GET | api/v1/<int:reviewId>/likes/ | 리뷰 좋아요 기능 |
    | POST | api/v1/<int:movieId>/review_create/ | 영화의 새로운 리뷰 생성 |
    | POST,DELETE | api/v1/<int:reviewId>/review_update/ | 리뷰 수정(POST),
    리뷰 삭제(DELETE) |
    | POST, PUT | api/v1/<int:movieId>/keyword/ | 영화 리뷰 키워드 DB에 저장(POST)
    영화 리뷰 키워드 수정&삭제(PUT) |
    | GET | api/v1/<int:reviewId>/get_comments/ | 리뷰의 모든 댓글 조회 |
    | GET | api/v1/<int:movieId>/recommend/ | 영화 별 추천 영화 조회 |
    | GET | api/v1/<int:movieId>/recommend_update/ | 영화 별 추천 영화 리스트 갱신 |
    | POST | api/v1/<int:reviewId>/comment_create/ | 리뷰의 새로운 댓글 생성 |
    | POST,DELETE | api/v1/<int:commentId>/comment_update/ | 댓글 수정(POST)
    댓글 삭제(DELETE) |
    | GET | api/v1/movie/<int:movieId>/likes/ | 영화 좋아요 기능 |
    | POST | api/v1/gernemovies/ | 장르 별 모든 영화 조회 |
    | POST | api/v1/moviesearch/ | 영화 검색 기능 |
    | GET | api/v1/<int:movieId>/wordcloud/ | 리뷰 키워드로 워드클라우드 생성 |

---

### 크롤링

- 왓챠피디아
    - 리뷰 키워드 기반 알고리즘 구현을 위한 데이터를 얻기 위하여 왓챠피디아 리뷰의 크롤링 진행
    - API를 따로 제공하지 않았기 때문
    - 리뷰 조회 화면이 스크롤 형태로 구성되어있었기 때문에 동적 크롤링을 위한 bf4, selenium 활용
    - 영화 데이터 1900개의 리뷰데이터 10만개 수집 진행
- 코드
    
    ```python
    import re
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time
    
    # 영화 이름에 따른 search_url 생성
    movie_name='어바웃 타임'
    movie_year='2013'
    movie_search_url=f'https://pedia.watcha.com/ko-KR/searches/movies?query={movie_name}'
    
    # search_url로 데이터 요청 -> html 변환
    movie_search_res=requests.get(movie_search_url)
    movie_search_html=BeautifulSoup(movie_search_res.content,'html.parser')
    
    # html의 검색기록에서 제일 위에 출력된 영화 상세정보를 보기 위한 movie_code 획득
    pick_movie=movie_search_html.select('#root > div > div.css-1xm32e0 > section > section > section > div.css-nzcouv-StyledResultsContainer-pageMarginStyle.e1493pgd1 > ul > li > a')
    
    for i in pick_movie:
        if i.select_one('a > div.css-zoy7di > div.css-qkf9j > div.css-h25two').get_text()[0:4]==movie_year:
            movie_code=i.attrs['href']
    
            # 얻은 movie_code로 그 movie의 comments_url 생성
            movie_comments_url=f'https://pedia.watcha.com{movie_code}/comments'
    
            browser = webdriver.Chrome('C:/chromedriver/chromedriver')
            browser.get(movie_comments_url)
    
            scroll_location = browser.execute_script("return document.body.scrollHeight")
    
            # 스크롤 10번 내림
    				# 충분한 리뷰 데이터를 얻기위함
    				# (위 사이트는 스크롤을 맨밑으로 내릴때마다 추가 정보를 불러오는 구조)
            for i in range(10):
              #현재 스크롤의 가장 아래로 내림
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                  
                #전체 스크롤이 늘어날 때까지 대기
                time.sleep(2)
                
                #늘어난 스크롤 높이
                scroll_height = browser.execute_script("return document.body.scrollHeight")
    
                #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
                if scroll_location == scroll_height:
                  break 
                else:
                  #스크롤 위치값을 수정
                  scroll_location = browser.execute_script("return document.body.scrollHeight")
    
            # 스크롤을 내린 page의 source를 받아주고, 셀레니움 창 종료
            html_res = browser.page_source
            browser.quit()
    
            # html 변환
            movie_comments_html = BeautifulSoup(html_res,'html.parser')
    
            # 한번에 불러와서 span까지 제거한 순수 내용만 출력
            movie_comments= movie_comments_html.select('#root > div > div.css-1xm32e0 > section > section > div > div > div > ul > div > div.css-4tkoly > a > div > span')
            for movie_comment in movie_comments:
               print(movie_comment.get_text())
    
          
            break
    ```
    
    ---
    

### 추천알고리즘

- 키워드 기반 영화 추천 알고리즘
    1. 활용
        - 영화 제목 키워드 기반 검색 알고리즘
        - 리뷰 키워드 기반 유사 영화 추천 알고리즘
    2. 코사인 유사도 알고리즘
        
        ```markdown
        - 코사인 유사도 알고리즘(Cosine Similarity Algorithm)은 두 벡터 간의 유사도를 측정하는 방법 중 하나입니다. 이 알고리즘은 두 벡터가 가리키는 각도의 코사인 값을 사용하여 유사도를 측정합니다. 두 벡터가 완전히 동일한 경우에는 코사인 값이 1이 되고, 서로 완전히 다른 경우에는 0이 됩니다.
        
        - 영화 추천 알고리즘에서는 리뷰 키워드를 기반으로 유사도를 측정합니다. 이를 위해 먼저 각 영화의 리뷰를 수집하고, 이를 토큰화하여 벡터로 변환합니다. 이후 유저가 선택한 영화의 리뷰 벡터와 다른 영화들의 리뷰 벡터 간의 코사인 유사도를 측정하여, 유사도가 높은 영화를 추천합니다.
        
        - 추천 알고리즘을 구현하기 위해 TF-IDF(Term Frequency-Inverse Document Frequency) 알고리즘을 사용하기도 합니다. 이 알고리즘은 각 단어의 빈도수와 역문서 빈도수를 곱하여 단어의 중요도를 측정합니다. 이를 통해 각 리뷰에 대한 키워드를 추출하고, 이를 기반으로 유사한 영화를 추천할 수 있습니다.
        ```
        
        - 데이터 전처리를 통해 영화 제목, 리뷰 데이터를 각각 키워드화 시킨 후 DB에 저장
            - API 스케쥴러를 통해 DB 갱신주기 설정
        - 코사인 유사도 공식을 통해 영화 1:1 비교 후 유사도 수치 0.3 이상인 결과만 받기
        - 출력된 결과 중 상위 10개 영화를 유사도 알고리즘으로 추천
            
            ```python
            import re
            import pandas as pd
            from pykospacing import Spacing
            from konlpy.tag import Okt
            okt = Okt()
            spacing=Spacing()
            ```
            
            ```python
            
            		def preprocess(text):
                    # 특수문자 제거
                    text = re.sub('[^가-힣]', '', text)
            				# 여백, 전처리
            				text = spacing(text)
                    # 형태소 분석
                    tokens = okt.nouns(text)
                    # 불용어 제거
                    stopwords = ['은', '는', '이', '가', '을', '를', '의', '에', '도', '와', '과', '으로', '로', '에서', '에게', '한', '하다','이고','영화','뭔가']
                    tokens = [token for token in tokens if token not in stopwords and len(token)>1]
                    return tokens
            
                # 코사인 유사도 계산
                def cosine_similarity(v1, v2):
                    dot_product = sum([a*b for a,b in zip(v1,v2)])
                    magnitude = math.sqrt(sum([a**2 for a in v1])) * math.sqrt(sum([b**2 for b in v2]))
                    if magnitude == 0:
                        return 0
                    else:
                        return dot_product / magnitude
            
            		A_text=''
            		B_text=''
            
            		A_tokens = preprocess(A)
            		B_tokens = preprocess(B)
            
                keywords = set(A_tokens+B_tokens)
                vectorA=[1 if keyword in A_tokens else 0 for keyword in keywords]
                vectorB=[1 if keyword in B_tokens else 0 for keyword in keywords]
            
                # 코사인 유사도 출력
            		cosine_similarity(vectorA, vectorB)
            		# 0 ~ 1 사이의 점수로 출력
            ```
            
    
1. 유저가 좋아요 한 영화의 리뷰 키워드와 비슷한 키워드를 갖는 영화 추천
2. 장르별 인기영화 Top10 랜덤 추천

---

### 워드클라우드

- 검색 및 추천 알고리즘 구현을 위한 키워드 분석 결과를 이용한 워드클라우드
- 

---

### 서비스 기능

1. 기본기능
    - 사용자 계정 관리
        - 회원가입
        - 로그인/로그아웃
        - 회원정보수정(비밀번호 변경)
        - 회원탈퇴
    - API 를 활용한 영화 데이터 접근
        - TMDB내 영화 데이터 사용 (무료)
    - 영화 상세 페이지
        - 줄거리/해당 장르/관객 평점/출연배우
    - 커뮤니티
        - 게시글 생성/수정/삭제
        - 댓글 생성/수정/삭제
    - 사용자 프로필
        - 유저 팔로우 기능 (본인 프로필 시 팔로워/팔로잉 수 확인가능)
2. 추가기능
    - 장르별 영화 조회
    - 영화 검색 기능
        - 영화 제목의 코사인 유사도 기반 검색 시스템
    - 영화 추천 기능
        - DB내 영화의 사용자 리뷰 데이터를 키워드 전처리하며, 추출한 키워드를 벡터화
        - 벡터화한 키워드를 코사인 유사도 분석으로 사용자 별 추천 영화 선정
    - 영화 좋아요(찜) 기능
    - 리뷰 좋아요 기능
    - 사용자 프로필 페이지 생성
        - 해당 유저의 활동(좋아요한 영화, 리뷰, 작성 리뷰 및 댓글) 관리 기능 추가
        - 워드클라우드 실시간 반응
    - 영화 상세페이지 내 다양한 서비스 기능 추가
        - 리뷰데이터 기반 워드 클라우드 제공
        - 사용자 리뷰 작성 시 실시간 업데이트 기능 생성
        - 영화별 Youtube 예고편 재생
        - 영화 배경 포스터 제공
    - 다크모드 구현

---

### 느낀점

✏️ 이성민

- 기능 개발 과정에서 DB의 변동이 될 거라 예상하여 ERD 설계를 개발 이후로 미뤘습니다. 물론 개발 과정에서 수많은 리팩토링을 거치며 DB가 자주 변동되었지만, 개발 초기의 DB 설계가 부족으로 무엇을 먼저 진행하여야 할지 갈피를 못 잡고 헤매는 시간이 길어지게 되었습니다. 온전한 ERD 설계하지는 않더라도 기초 뼈대가 되는 정도의 설계만큼은 탄탄하게 선행한 후에 개발해야 한다는 것을 느꼈습니다.
- 협업에 있어서 의사소통 능력의 중요성을 깨닫게 되는 계기가 되었습니다.
- 한정된 시간에서 개발을 진행함에 불구하고 기능에 대한 욕심이 생겨서 이것저것 일정에 추가하려고 했었는데, 계획되지 않은 개발은 오히려 오류를 해결하는데 긴 시간을 쓰게 만들어 이도 저도 아니게 됨을 느꼈습니다.

✏️ 송지윤

- 싸피에 들어오기 전 데이터 분석과 개발이 흐름적으로는 유기적으로 연결이 되어있지만, 실제 코드에는 별개로 작동하고 짜여질 거라 생각했었다. 하지만, 우리가 사용하는 수많은 서비스 및 플랫폼은 다양한 알고리즘 기반으로 구성되어있다는 것을 미처 생각하지 못하고 있었다. 막상 알고리즘을 적용할 수 있다니 이번 프로젝트에서 적용해보는 기회가 있어서 좋았지만, 막상 어떻게 작성하지 보다 어디에 어떻게 작성해서 차리를 해줘야지? 라는 새로운 의문이 생기게 되었다. 결론은 간단했다! 데이터 분석은 파이썬의 pandas 라이브러리 내에서 주로 다루고, 우리 프로젝트의 backend 프레임워크인 django에는 views.py가 있었던 것이다. 어렵게 생각하지 않고 필요한 내용과 데이터를 view에서 알고리즘 함수로 처리해주면 된다는 것을 알게 되었다. 개발은 상호작용 이라는 것.!!✨
- `APS-scaduler`
    - 우리는 크롤링을 진행하게 되면서 데이터 양이 서버를 실행시킬 때마다 혹은 새로고침을 할때마다 데이터가 갱신되게 되었을때 프로그램이 많이 무거워지고, 데이터 처리에 소요되는 시간으로 사용자 요청에 즉각적 응답이 어려울 수 있어 갱신 주기에 대해 고려를 하게 되면서 장고의 APS스케쥴러기능에 대해 알 수 있게 되었다. 적용해보면서 데이터가 DB에 저장되고 연결되는 흐름을 보다 쉽게 이해할 수 있었다.
    - 주로 프로젝트에서 데이터 갱신은 cron으로 많이 적용한다고 하는데, cron은 리눅스 환경의 스케쥴러였기 때문에 장고 버전의 스케쥴러를 사용하게 되었다.
- `vue-axios & props` & `emit`
    - 1학기 진도를 나가며 vue를 가장 마지막에 배우기도 하고 진도가 보다 빠른 편이여서 완벽히 구조를 이해하고 프로젝트를 시작하지 못했다.(기능과 개념만 아는정도)
    - 후반부에 단기간으로 습득해야 했던 axios를 통한 요청과 응답을 프로젝트에서는 상당히 많이 작성해야 했고, 초반부 페어와 역할을 각각 나누지 않고 vue와 django를 상호 체크 하면서 코드를 작성했기 때문에 요청에 대한 순서와 흐름을 설명을 들으면서 잘 이해할 수 있개 되었다.
- `코드리팩토링` 가장 많은 지식과 시간을 요구한다는 것을 다시 한번 깨닫게 되었다. 

---

### 프로젝트 진행 일정

- 아래와 같이 진행하고자 하였다.

📍 기획

1. 그라운드 룰 & 컨벤션 정하기
    1. 프로젝트 수행 역할
    2. 커밋메세지 작성 방법 통일
    3. readme 작성 법 상의
    4. 코드 스타일
    
2. 구체적 방향성 및 방법론
    1. 주제 선정 `what`
        1. 사용자 리뷰 분석 강조할 수 있는 주제/제목 필요
    2. 주제 선정에 대한 타당성 `why`
    3. 방법론 `how`
        1. 애자일 방법론
        2. 어떤 기술 스택을 사용할 것인지
            1. `django` `Vue`
        3. 모델링 구상
            1. 큰 틀만 우선적으로 
            2. 마지막 순서로 erd 그리기
            3. User
        4. 구체적 컨벤션 작성 → 변수, 전처리, DB …
        
3. 기본적인 구조 작성
    1. 큰 틀에서의 기능(기본 기능)
    2. CRUD 구성
    3. 데이터 베이스 모델 구조
        1. ERD  
4. 디자인
    1. 레이아웃 상의
        1. 참고 할 만한 사례 공유
        2. 기본적인 배치 및 구조 결정
    2. UI / UX 디자인 초안 잡기
        1. 디자인 툴 사용
        
    3. 반응형 웹 페이지 구성
    
    | 05/16_화 | 05/17_수 | 05/18_목 | 05/19_금 |
    | --- | --- | --- | --- |
    | ◾ 기본 페이지 별 기능 상의 및 결정
    ◾ 초기 화면 구성(디자인 배치)
    ◾ 알고리즘 종류, 방식 회의
    ◾ 결정사항 문서화 하기 | ◾ start project 프로젝트 생성
    ◾ CRUD 우선 구현
        → 대략적인 화면 디자인
        → 기초 구조 설계 후 차근차근 프로젝트 쌓아나가기 위함
    ◾ MoviewView에 가장 많은 라우터와 데이터가 담기기 때문
    → 라우터 설정 및 갱신에 대한 공부 | ◾데이터 첫 호출 → 사용할 데이터 개수 결정
    ◾ 데이터베이스 API에서 받아와서 만들기
    ◾ 사용자 관련 기능 구현
    → 회원가입/로그인/로그아웃 구현
    ◾ token에 따른 화면 구성
    ◾ CRUD(review/opinion) 나머지 구성  | ◾ debate
    ◾ 크롤링데이터 100p기준 (약1900개)
    ◾ 새로고침 문제 해결 
    ◾Django apps scheduler(cron)
    ◾readme 정리하기(진도/상황/정리/ 등등)
    ◾CSS
    → 일주일 기한 동안 CSS에 대한 고민 및 결정 사항이 생겨야 할 시점
    ◾review 및 debate child
    → 구현하고 싶었던 기능이지만 child를 통한 데이터 전송 개념 이해가 어려웠다.
    ◾홈 화면 배너 설정 |
    | 05/22_월 | 05/23 | 05/24 | 05/25 |
    | ◾ 장르별 영화목록 구현(최신순, 인기순)
    ◾ 토론방 → 모달창 만들어서 리뷰의 댓글 개념으로 구성
    ◾ 회원정보수정
    ◾ 리뷰수정/삭제
    —————————
    ◾ 회원탈퇴
    ◾ 유저 프로필 (우선순위 고려) | ◾ 팔로워 기능 구현 (유저의 프로필 화면 내에서)
    1. 팔로워 기능
    2. 팔로잉 기능
    3. 유저의 팔로워 및 팔로우 리스트 목록 구현
    ◾ 리뷰 댓글 모달창 수정(영화리뷰를 클릭하면 리뷰 모달창이 열리면서 댓글 작성하는 모달 기능)
    ➡ 더보기를 스크롤로(영화 리뷰 길이가 차이가 있기 때문에 리뷰에서는 댓글을 ...으로 줄이고) >> 긴 댓글의 경우 모달창 넘어가는 문제 해결
    ◾ 유저 프로필 화면에서 사용자 활동 확인 기능 구현(모달)
    1. 사용자가 작성한 리뷰
    2. 사용자가 작성한 리뷰 댓글
    3. 사용자가 좋아요 누른 영화 목록
    ➡ 사용자가 작성한 댓글을 클릭하면 해당 모달창으로 넘어갈 수 있는 기능 (오늘 할일 중에서는 우선 순위 (하))
    -------------점심시간
    ◾ 추천 알고리즘
    1. 왓챠피디아 크롤링 데이터 ✅
    a. 왓챠피디아의 리뷰데이터 크롤링(bf4, selenium 활용)
    2. 리뷰데이터 push -> json loaddata ✅
    a. 크롤링 한 데이터 전처리 진행 후 json파일로 로드
    3. 키워드 DB 생성 및 추가 (진행예정) ✅
    4. 데이터 전처리를 통해 기존의 리뷰 데이터에서 키워드 추출 후 별도 DB로 저장
    5. 유사도 검사 알고리즘 구현(코사인 유사도 활용 예정)
    a. 알고리즘 구현을 위한 자료 조사 ✅ ex. 타 리뷰 활용 프로젝트
    b. 추천 결과는 Home에서 보여줄 예정
    c. 위에서 작성 및 완료된 코사인 유사도를 활용하여 검색 알고리즘에 사용(재사용)
    d. 검색 결과 컴포넌트 추가 (UI는 완료, 컴포넌트 생성 예정)
    --------------남는 시간
    ◾ CSS 시간 투자 | ✅ 해결된 TODO
    ————————————————————-
    TO DO LIST_우선순위
    ◾ 알고리즘
    1. 유사도 검사 알고리즘 구현
        ➡ 검색 알고리즘 (코사인 유사도 활용 예정/ 코드 있음)✅
    2. 영화 추천 알고리즘
        ➡ 어제 키워드 추출 및 전처리 후 DB 저장 완료 > 워드클라우드 화 완료 > 리뷰 페이지에 넣기 완료 ✅
              문제 발생 💥💥💥 
         ———
        ➡ TF_IDF 활용 → 벡터화 후 코사인으로만 활용
        ➡ 코드는 작성되어있고, 적용해서 돌리는 작업 필요 (흐름 이해)
        ➡ 어제처럼 코드 실행 시 오류 발생 시간 고려
        ➡ 검색 결과 컴포넌트 생성 ✅
    
    ◾ 모달 오류 수정
    1. 리뷰item 수정/삭제 오류 ✅
        ➡ CSS 디자인 때문에 코드 위치 수정 한 영향으로 오류 발생
    2. 댓글 생성시 반응 안하는 오류
    3. 리뷰
    
    ◾ CSS(기본 레이아웃만 짜여있는 상태)
    1. 사이트 접속 화면(로고화면)
    2. 로그인/회원가입 화면
    3. 회원정보수정
    4. 영화 카드(movieitem)
        ➡ 제목을 카드 뒷면으로 
        ➡ 뒷면 디자인(그라데이션)
    ——————————————————(퇴근 전 까지)
    5. 메인 홈 화면 배너
        ➡ 동영상 or 사진
    6. 검색창
    
    ◾ 자잘한 오류 및 css
      | ◾ erd |

---