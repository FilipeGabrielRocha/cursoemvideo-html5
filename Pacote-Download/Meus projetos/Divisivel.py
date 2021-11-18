div2 = num % 2
div3 = ((num // 1 % 10) + (num // 10 % 10) + (num // 100 % 10) + (num // 1000 % 10)) % 3
div4 = ((num // 1 % 10) + (num // 10 % 10)) % 4 or num % 4
div5 = (num // 1 % 10) % 5
div6 = (((num // 1 % 10) + (num // 10 % 10) + (num // 100 % 10) + (num // 1000 % 10)) % 3) or num % 2