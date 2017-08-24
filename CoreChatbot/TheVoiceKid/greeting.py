

def greeting(sender_id):
    loi_chao = "Chào bạn. Tại đây bạn có thể cập nhật những tin tức nóng hổi, cũng như tham gia bình chọn cho thí sinh mình yêu thích nhất. Hãy bắt đầu bằng việc nhấn vào nút Home bên dưới hoặc bất cứ lúc nào bạn gõ 'home' hoặc 'menu' để quay về tính năng chính nha."
    buttons = [
        Template.ButtonPostBack(
            "Home", "home")
    ]
    page.send(sender_id, Template.Buttons(loi_chao, buttons))
