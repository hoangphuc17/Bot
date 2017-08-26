# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page


def timeline(sender_id):
    text = "📣📣📣 Chương trình “Giọng Hát Việt Nhí” 2017 sẽ được phát sóng vào lúc 9h10 tối thứ 7 hằng tuần từ (ngày 12/08/2017) trên kênh VTV3"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))


def introduce(sender_id):
    text = "Đến hẹn lại lên, 'Giọng Hát Việt Nhí' đã trở lại và lợi hại hơn bao giờ hết. Với dàn huấn luyện viên là những nghệ sỹ trẻ nổi tiếng tài năng và sở hữu lượng fan hùng hậu nhất nhì làng giải trí Việt. Đó là cặp đôi Hương Tràm –Tiên Cookie, ca sĩ – nhạc sĩ Vũ Cát Tường, ca sĩ Soobin Hoàng Sơn. Họ hứa hẹn sẽ mang đến cho Giọng Hát Việt Nhí mùa 5 nhiều điều thú vị với độ cạnh tranh, “chặt chém” quyết liệt trên ghế nóng.\n📣📣📣 21h10 thứ 7 hằng tuần trên kênh VTV3 - Giọng Hát Việt Nhí 2017 với những bất ngờ đang chờ bạn khám phá!"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))
