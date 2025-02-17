def digits(total_pages):
    digit_count = 0
    current_page = 1
    digit_length = 1
    
    while current_page <= total_pages:
        next_page = current_page * 10
        pages_in_range = min(total_pages + 1, next_page) - current_page
        digit_count += pages_in_range * digit_length
        current_page = next_page
        digit_length += 1
    
    return digit_count

def digits_range(start_page, end_page):
    digit_count = 0
    current_page = 1
    digit_length = 1
    
    while current_page <= end_page:
        next_page = current_page * 10
        pages_in_range = min(end_page + 1, next_page) - max(start_page, current_page)
        if pages_in_range > 0:
            digit_count += pages_in_range * digit_length
        current_page = next_page
        digit_length += 1
    
    return digit_count

def search(start_page, end_page, total_digits):
    previous_digits = digits_range(1, start_page - 1)
    
    while start_page <= end_page:
        mid_page = (start_page + end_page) // 2
        
        current_digits = previous_digits + digits_range(start_page, mid_page)
        remaining_digits = total_digits - current_digits
        
        if current_digits == remaining_digits:
            return mid_page
        elif current_digits < remaining_digits:
            start_page = mid_page + 1
            previous_digits = current_digits
        else:
            end_page = mid_page - 1
    
    return end_page

def page(total_pages):
    total_digits = digits(total_pages)
    return search(1, total_pages, total_digits)

while True:
    user_input = int(input())
    if user_input == 0:
        break
    print(page(user_input))