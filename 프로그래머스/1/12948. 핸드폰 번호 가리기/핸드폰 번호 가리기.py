def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4] + phone_number[-3] + phone_number[-2] + phone_number[-1]