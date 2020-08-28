class PostPage:
    ADD_COMMENT_BUTTON = '#add-comment'
    APPROVE_COMMENT_BUTTON = '#approve-comment'
    DELETE_POST_BUTTON = '#delete-post'

    def __init__(self, page_driver):
        self.driver = page_driver

    def new_comment(self):
        self.driver.click(self.ADD_COMMENT_BUTTON)

    def approve_comment(self):
        self.driver.click(self.APPROVE_COMMENT_BUTTON)

    def delete_post(self):
        self.driver.click(self.DELETE_POST_BUTTON)
