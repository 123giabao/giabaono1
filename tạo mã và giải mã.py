# # Mã hóa thông điệp
# def encode_message(message):
#     encoded = ""
#     for char in message:
#         encoded += chr(ord(char) + 3)  # Dịch chuyển ký tự lên 3 vị trí trong bảng mã ASCII
#     return encoded

# # Giải mã thông điệp
# def decode_message(encoded_message):
#     decoded = ""
#     for char in encoded_message:
#         decoded += chr(ord(char) - 3)  # Dịch chuyển ký tự xuống 3 vị trí trong bảng mã ASCII
#     return decoded

# # Thử nghiệm
# message_to_encode = "đợi tới lúc đó bà có đồng ý hong"
# encoded_message = encode_message(message_to_encode)
# print(f"Encoded message: {encoded_message}")

# decoded_message = decode_message(encoded_message)
# #print(f"Decoded message: {decoded_message}")
# print(f"Decoded message: **************************************")

def decode_message(encoded_message):
    decoded = ""
    for char in encoded_message:
        decoded += chr(ord(char) - 3)  # Dịch chuyển ký tự xuống 3 vị trí trong bảng mã ASCII
    return decoded

# Thử nghiệm
encoded_message = "ĔỦl#wỞl#oýf#Ĕö#eã#fö#ĔỖqj#Ā#krqj"
decoded_message = decode_message(encoded_message)
print(f"Decoded message: {decoded_message}")
