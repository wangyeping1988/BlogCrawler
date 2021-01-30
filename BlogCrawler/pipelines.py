# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import re
import urllib2


class BlogcrawlerPipeline(object):
    def process_item(self, item, spider):
        try:
            rstr = r"[\/\\\:\*\?\"\<\>\|]"
            post_file = codecs.open('posts' + os.path.sep + re.sub(rstr, "_", item['title']) + '.md', 'wb', encoding='utf-8')
            post_file.write(item['content'])
            post_file.close()
        except(IndexError, TypeError):
            pass

        return item

class Kie4crawlerPipeline(object):
    def process_item(self, item, spider):
        try:
            for link in item['links']:
                print("Enter Kie4crawlerPipeline---------")
                print("link---------" + link)
                # https://img.i1m2g3e.com/passimg/tx/72811/01.jpg
                parts = link.split('/')
                print("parts---------" + ''.join(parts))
                # link[2:len(post_content)]
                category = parts[len(parts) - 3]
                print("category---------" + category)
                id = parts[len(parts) - 2]
                print("id---------" + id)
                fileName = parts[len(parts) - 1]
                print("fileName---------" + fileName)
                number = fileName[0:(len(fileName) - len('.jpg'))]
                print("number---------" + number)
                rstr = r"[\/\\\:\*\?\"\<\>\|]"
                folder = 'images' + os.path.sep + id + "_" + item['title']
                # self.mkdir(folder.encode("utf-8"))
                print("folder---------" + folder)
                self.mkdir(folder)
                print("prepare filePath")
                filePath = folder + os.path.sep + fileName
                print("filePath---------" + filePath)
                self.download_img(link, filePath)
        except Exception as ex:
            print(ex)
            pass

        return item

    def mkdir(self, path):
        # 引入模块
        import os
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            print("path---------" + path)
            os.makedirs(path)
            # print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            # print(path + ' 目录已存在')
            return False

    def download_img(self, img_url, filename):
        print("img_url---------" + img_url)
        print("filename---------" + filename)
        request = urllib2.Request(img_url)
        try:
            response = urllib2.urlopen(request)
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())  # 将内容写入图片
                return filename
        except:
            return "failed"

    def download_img_with_token(img_url, api_token):
        header = {"Authorization": "Bearer " + api_token}  # 设置http header
        request = urllib2.Request(img_url, headers=header)
        try:
            response = urllib2.urlopen(request)
            img_name = "img.png"
            filename = "C:\\Users\\cloudoxou\\Desktop\\" + img_name
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())  # 将内容写入图片
                return filename
        except:
            return "failed"