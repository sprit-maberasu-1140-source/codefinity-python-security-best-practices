import logging

def log_user_action(user_id, action, details):
    # フィルタリング：機密情報キーを除外
    safe_details = {
        k: v for k, v in details.items()
        if k not in ['password', 'ssn', 'credit_card', 'secret']
    }
    # ログメッセージ作成
    log_message = f"User {user_id} performed action: {action} | Details: {safe_details}"
    # INFOレベルで出力
    logging.info(log_message)
    return log_message

details_1 = {
    "ip": "192.168.1.1",
    "location": "NYC",
    "password": "hunter2"
}
result_1 = log_user_action("user123", "login_attempt", details_1)
print(result_1)

details_2 = {
    "email": "jane@example.com",
    "ssn": "123-45-6789",
    "action_desc": "changed email"
}
result_2 = log_user_action("user456", "update_profile", details_2)
print(result_2)