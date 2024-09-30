from apps.core.repositories.blog_repository import BlogPostRepository

class BlogPostService:
    @staticmethod
    def list_all_posts():
        return BlogPostRepository.get_all_posts()

    @staticmethod
    def retrieve_post(post_id):
        return BlogPostRepository.get_post_by_id(post_id)

    @staticmethod
    def create_new_post(data):
        return BlogPostRepository.create_post(data)

    @staticmethod
    def update_existing_post(post_id, data):
        return BlogPostRepository.update_post(post_id, data)

    @staticmethod
    def delete_existing_post(post_id):
        BlogPostRepository.delete_post(post_id)
