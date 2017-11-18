import os
import sys
from CoreChatbot.cbtest.cbtest_database import *


# def add_faq3():
#     faq3_level_1('test', '1', ['tổ chức', 'diễn ra'])
#     faq3_level_2('test', '1', '11', ['địa điểm', 'ở đâu', 'tại', 'chỗ', 'nơi'])
#     faq3_answer('test', '11', '179 LCT')

#     faq3_level_1('test', '1', ['tổ chức', 'diễn ra'])
#     faq3_level_2('test', '1', '12', ['khi', 'lúc', 'bao', 'giờ', 'thời điểm'])
#     faq3_answer('test', '12', 'Tháng 10 hàng năm')

#     faq3_level_1('test', '2', ['địa điểm', 'nơi', 'chỗ'])
#     faq3_level_2('test', '2', '21', ['quay', 'ghi'])
#     faq3_answer('test', '21', '5B NDC')

#     faq3_level_1('test', '2', ['địa điểm', 'nơi', 'chỗ'])
#     faq3_level_2('test', '2', '22', [
#                  'tham gia', 'đăng kí', 'đăng ký', 'tham gia'])
#     faq3_answer('test', '21', 'chỉ ở TPHCM')


# add_faq3()

def add_faq3_list():
    faq3_list(['tổ chức', 'diễn ra'], ['địa điểm',
                                       'ở đâu', 'tại', 'chỗ', 'nơi'], '179 LCT')
    faq3_list(['tổ chức', 'diễn ra'], ['khi', 'lúc', 'bao',
                                       'giờ', 'thời điểm'], 'Tháng 10 hàng năm')
    faq3_list(['địa điểm', 'nơi', 'chỗ', 'ở đâu'],
              ['quay', 'ghi hình'], '5B NDC')
    faq3_list(['địa điểm', 'nơi', 'chỗ', 'ở đâu'], ['tham gia', 'tuyển sinh',
                                                    'đăng kí', 'đăng ký', 'tham gia'], 'chỉ ở TPHCM')


add_faq3_list()
