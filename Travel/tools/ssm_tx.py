from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
#腾讯云sdk发短信
def ssm(phone,g_name,g_type,menoy,time):
    appid = 1400*****  # SDK AppID 以1400开头
    # 短信应用 SDK AppKey
    appkey = "e6++++++++8d106****c"
    # 需要发送短信的手机号码
    template_id = 375220  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
    # 签名
    sms_sign = '乐途网提醒'  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

    phone_numbers = [phone]

    sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
    params = [g_name,g_type,menoy, time]

    ssender = SmsSingleSender(appid, appkey)
    try:
        result = ssender.send_with_param(86, phone_numbers[0],
                                         template_id, params, sign=sms_sign, extend="", ext="")
        return result
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

