#!/usr/bin/python
# fileencoding=utf-8

# 路由前缀不能以auth/开头


def get(options):
    return [
        (r'/data/img/(.*)', 'eslib.request_handlers.ResourceHandler',
         {'path': options.img_data_path, 'valid_file_types': ['jpg', 'bmp', 'png', 'gif', 'tif',
                                                              'jpeg']}),
        (r'/data/audio/(.*)', 'eslib.request_handlers.ResourceHandler',
         {'path': options.audio_data_path, 'valid_file_types': ['mp3', 'wma']}),
        (r'/data/video/(.*)', 'eslib.request_handlers.ResourceHandler',
         {'path': options.video_data_path, 'valid_file_types': ['flv', 'mp4']}),
        (r'/data/pdf/(.*)', 'eslib.request_handlers.ResourceHandler',
         {'path': options.pdf_data_path, 'valid_file_types': ['pdf']}),

        (r'/auth/send_reset_password_email', 'klxlib.apps.login.SendResetPasswordMail'),
        (r'/auth/phone_reset_password', 'klxlib.apps.login.PhoneResetPassword'),
        (r'/auth/check_username', 'klxlib.apps.login.CheckUsernameHandler'),
        (r'/auth/check_email', 'klxlib.apps.login.CheckEmailHandler'),
        (r'/auth/check_mobile_number', 'klxlib.apps.login.CheckMobileNumberHandler'),
        (r'/auth/check_mobile_identify', 'klxlib.apps.login.CheckMobileNeedIdentifyHandler'),

        (r'/auth/get_new_identify_image', 'klxlib.apps.user.GenNewIdentifyImageHandler'),
        (r'/auth/identify_image/(\w+)', 'klxlib.apps.user.IdentifyImageHandler'),

        (r'/auth/login', 'klxlib.apps.login.AuthLogin'),
        (r'/auth/logout', 'klxlib.apps.login.AuthLogout'),
        (r'/auth/signup', 'klxlib.apps.login.AuthSignup'),
        (r'/auth/signup_agreement', 'klxlib.apps.login.SignupAgreementHandler'),

        (r'/auth/compensation_success', 'klxlib.apps.user.CompensationSuccessHandler'),

        (r'/auth/trial', 'klxlib.apps.user.CreatNewTrialUser'),

        (r'/auth/decode_cookie', 'klxlib.apps.login.DecodeCookieHandler'),

        (r'/auth/signup_success', 'klxlib.apps.login.AuthSignupSuccess'),
        (r'/auth/send_reset_password_success', 'klxlib.apps.login.SendResetPasswordSuccess'),

        (r'/auth/register_auth', 'klxlib.apps.login.RegisterEmailAuth'),
        (r'/auth/reset_password_auth', 'klxlib.apps.login.ResetPasswordAuth'),
        (r'/auth/phone_reset_password_auth', 'klxlib.apps.login.PhoneResetPasswordAuth'),

        (r'/auth/from_third_party', 'klxlib.apps.login.AuthFromThirdPartyHandler'),
        (r'/auth/from_eduyun', 'klxlib.apps.login.AuthFromEduyunHandler'),

        (r'/switch_subject', 'klxlib.apps.login.SwitchSubjectSiteHandle'),

        (r'/klx/order/alipay_return', 'klxlib.apps.order.AlipayOrderReturnHandler'),
        (r'/klx/order/alipay_notify', 'klxlib.apps.order.AlipayOrderNotifyHandler'),
        (r'/klx/order/mobile_alipay_notify', 'klxlib.apps.order.MobileAlipayCallbackHander'),
        (r'/klx/order/agent_pay_notify', 'klxlib.apps.order.AgentPayNotifyHandler'),

        (r'/apps', 'klxlib.apps.misc.KlxAppsHandler'),
        (r'/apps/(\w+)/(\w+)/dl', 'klxlib.apps.misc.KlxAppsDownloadDispachHandler'),

        (r'/click', 'klxlib.apps.login.ClickStatHandler'),

        (r'/about', 'klxlib.apps.misc.AboutHandler'),
        (r'/contact', 'klxlib.apps.misc.ContactUsHandler'),
        (r'/jobs', 'klxlib.apps.misc.JobsHandler'),
        (r'/app', 'klxlib.apps.misc.AppHandler'),
        (r'/apk', 'klxlib.apps.misc.ApkHandler'),
        (r'/links', 'klxlib.apps.misc.LinksHandler'),

        (r'/jiajiao', 'klxlib.apps.misc.JiajiaoHandler'),

        (r'/platform/service/xxt', "klxlib.apps.platform.xxt.XXTMsgHandler"),

        (r'/user/register', "klxlib.apps.app.user.UserRegisterHandler"),
        (r'/user/third_register', "klxlib.apps.app.user.ThirdUserRegisterHandler"),
        (r'/user/get_verify_code', "klxlib.apps.app.user.UserFetchVerifyCodeHandler"),
        (r'/user/login', "klxlib.apps.app.user.UserLoginHandler"),
        (r'/user/modify_password_by_phone',
         "klxlib.apps.app.user.UserModifyPasswordByPhoneHandler"),
        (r'/user/modify_password',
         "klxlib.apps.app.user.UserModifyPasswordHandler"),
        (r'/user/(.*)', "klxlib.apps.app.user.UserInfoHandler"),

        (r'/add_feedback', 'klxlib.apps.feedback.AddFeedbackHandler'),
        (r'/auth/sign_success', 'klxlib.apps.login.AppAuthSignupSuccess'),

        (r'/share_paper/(\w+)/share', 'klxlib.apps.paper.SharePaperHandler'),
        (r'/share_paper/papers', 'klxlib.apps.paper.SharePaperBatchHandler'),
        (r'/share_papers/status', 'klxlib.apps.paper.GetPaperShareStatusBatchHandler'),

        # add to build signup and reset password
        (r'/mobile/teacher/index', 'klxlib.apps.user.MobileTeacherMainHandler'),
        (r'/mobile/student/index', 'klxlib.apps.user.MobileStudentMainHandler'),
        (r'/mobile/login', 'klxlib.apps.login.MobileUserLoginHandler'),
        (r'/mobile/signup', 'klxlib.apps.login.MobileUserSignupHandler'),
        (r'/mobile/user_protocol', 'klxlib.apps.login.MobileUserProtocol'),
        (r'/mobile/email_passwod_reset', 'klxlib.apps.login.MobileEmailPasswordReset'),
        (r'/mobile/phone_password_reset', 'klxlib.apps.login.MobilePhonePasswordReset'),

        # 试卷收藏
        (r'/collect_item', 'klxlib.apps.item.CollectItemHandler'),
        (r'/cancel_collect_item', 'klxlib.apps.item.CancelCollectItemHandler'),
        (r'/my_favorites', 'klxlib.apps.item.MyFavoriteHandler'),

        (r'/account/main', 'klxlib.apps.account.AccountMainHandler'),
        (r'/account/student_mgt', 'klxlib.apps.account.AccountStudentMgtHandler'),
        (r'/account/add_new_branch', 'klxlib.apps.account.AddNewAccountBranchHandler'),
        (r'/account/add_new_role', 'klxlib.apps.account.AddNewAccountRoleHandler'),
        (r'/account/(\w+)/delete_branch', 'klxlib.apps.account.DeleteAccountBranchHandler'),
        (r'/account/(\w+)/delete_role', 'klxlib.apps.account.DeleteAccountRoleHandler'),
        (r'/account/(\w+)/add_teacher_role', 'klxlib.apps.account.SetTeacherUserRoleHandler'),
        (r'/account/(\w+)/add_student_branch', 'klxlib.apps.account.SetStudentUserBranchHandler'),
        (r'/account/(\w+)/delete_teacher_role', 'klxlib.apps.account.DeleteTeacherUserRoleHandler'),
        (r'/account/(\w+)/delete_student_branch',
         'klxlib.apps.account.DeleteStudentUserBranchHandler'),
        (r'/account/(\w+)/update_branch_name',
         'klxlib.apps.account.UpdateAccountBranchNameHandler'),
        (r'/account/(\w+)/update_role_name', 'klxlib.apps.account.UpdateAccountRoleNameHandler'),
        (r'/account/(\w+)/update_role_subject',
         'klxlib.apps.account.UpdateAccountRoleSubjectHandler'),
        (r'/account/get_teacher_in_school', 'klxlib.apps.account.GetTeacherInSchoolHandler'),
        (r'/account/(\w+)/get_student_in_branch', 'klxlib.apps.account.GetStudentInBranchHandler'),
        (r'/account/get_student_in_school', 'klxlib.apps.account.GetStudentInSchoolHandler'),
        (r'/account/batch_add_students', 'klxlib.apps.account.AccountCreateStudentHandler'),
        (r'/account/(\w+)/set_student_number', 'klxlib.apps.account.SetStudentNumberHandler'),
    ]
