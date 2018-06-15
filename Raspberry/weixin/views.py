# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
#create my weixin code 
WECHAT_TOKEN='helloworld'
AppID = 'wxf96fcb3648a97871'
AppSecret = 'b6da20cc8bd53143fcdb26a1e3f02577'
#实例化WchatBasic
wechat_instance = WechatBasic(token=WECHAT_TOKEN,appid=AppID,appsecret=AppSecret);

@csrf_exempt
def index(request):
    if request.method == 'GET':
        #检验合法性
        #从request 中提取基本信息
        signature = request.GET.get('signature');
        timestamp = request.GET.get('timestamp');
        nonce = request.GET.get('nonce');
        if not wechat_instance.check_signature(signature = signature,
                timestamp = timestamp,nonce = nonce):
            return HttpResponseBadRequest('验证失败');
        return HttpResponse(request.GET.get('echostr',''),content_type="text/plain");
    #解析本次请求的XML数据
    try:
        wehchat_instance.parse_data(data=request.body);
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data');
    #获取解析好的微信请求信息
    message = wechat_instance.get_message();
    #关注事件以及不匹配时的默认恢复
    response = wechat_instance.response_text(
            content = ('感谢您的关注')
            );
    if isinstance(message,TextMessage):
        #当前会话内容
        content = message.content.strip();
        if content == '功能':
            replay_text = ('查看温湿度','获取获取绿植照片','浇水');
        response = wechat_instance.response_text(content=replay_text);
    return HttpResponse(response,content_type="application/xml");
