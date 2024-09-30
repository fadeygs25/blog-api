from apps.core.models import BlogPost

class BlogPostRepository:
    @staticmethod
    def get_all_posts():
        return BlogPost.objects.all()

    @staticmethod
    def get_post_by_id(post_id):
        return BlogPost.objects.get(id=post_id)

    @staticmethod
    def create_post(data):
        return BlogPost.objects.create(**data)

    @staticmethod
    def update_post(post_id, data):
        post = BlogPostRepository.get_post_by_id(post_id)
        for key, value in data.items():
            setattr(post, key, value)
        post.save()
        return post

    @staticmethod
    def delete_post(post_id):
        post = BlogPostRepository.get_post_by_id(post_id)
        post.delete()
