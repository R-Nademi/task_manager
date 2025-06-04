import os
import pickle

# نام فایل داده‌ها
file_name = "ticket.dat"

# بررسی وجود فایل
def check_file():
    return os.path.exists(file_name)

# تابع خواندن داده‌ها از فایل
def read_from_file():
    if check_file():
        try:
            # اگر فایل خالی نباشد، داده‌ها را بخوان
            if os.path.getsize(file_name) > 0:
                with open(file_name, "rb") as file:
                    return pickle.load(file)
            else:
                # فایل خالی است
                return []
        except Exception as e:
            print(" !!! خطا در خواندن فایل:", e)
            # اگر فایل خراب باشد، حذف و ساخت مجدد فایل
            os.remove(file_name)
            open(file_name, "wb").close()
            return []
    else:
        # اگر فایل وجود ندارد، آن را بساز و لیست خالی برگردان
        open(file_name, "wb").close()
        return []

# تابع نوشتن داده‌ها در فایل
def write_to_file(data_list):
    with open(file_name, "wb") as file:
        pickle.dump(data_list, file) # noqa