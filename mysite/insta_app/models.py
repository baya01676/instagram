from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    url_network = models.URLField(null=True, blank=True)
    is_official = models.BooleanField(default=False)
    phono_number = PhoneNumberField(null=True, blank=True)
    data_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Follow(models.Model):
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')


class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=100)

class Post(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    music = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    hashtag = models.ManyToManyField(Hashtag, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(UserProfile, blank=True, related_name='post_user')

    def __str__(self):
        return f'{self.user},{self.description}'


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_contents')
    file = models.FileField()


class PostLike(models.Model):
    users = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ['users','post']

    def __str__(self):
        return f'{self.post},{self.users}'


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.post_comment}'

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user','comment']

    def __str__(self):
        return f'{self.user}'


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_favorite')

class Chat(models.Model):
    people = models.ManyToManyField(UserProfile)
    created_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    video = models.FileField(upload_to='videos',null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

