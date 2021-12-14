from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model): #modes의 Model을 상속받아 정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author(저자) : ForeignKey(외래키)로 정의/ 글을 작성한 사람 의미. 외래키로 설정->AUTH_USER_MODEL에 있음
    # on_delete=models.CASCADE를 통해 얘가 삭제 될 때에 연관된 다른 필드들도 삭제되도록 함.
    title = models.CharField(max_length=200)
    # 블로그의 제목. models의 CharField로 설정.
    text = models.TextField()
    # 글에 관한 것.
    created_date = models.DateTimeField(
        default=timezone.now) # 디폴드 값. 처음 게시글이 생성된 시간을 의미
    published_date = models.DateTimeField(
        blank=True, null=True) # 게시글이 게시된 시간을 의미

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # 게시글이 저장될 수 있는 시간

    def __str__(self):
        return self.title # 타이틀 리턴하도록 설정
