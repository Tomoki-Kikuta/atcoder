def main():
    N = int(input())
    trafic = []
    for i in range(5):
        a = int(input())
        trafic.append(a)
    now_time = 0
    now_people = N
    number_of_people = 0
    for i in range(5):
        if i != 0:
            if number_of_people == 0:
                number_of_people = trafic[i-1]
            now_people = number_of_people + max((N - number_of_people)  - trafic[i] * (now_time - i),0)
        number_of_people = now_people % trafic[i]
        now_time += -(-now_people // trafic[i]) ## 小数点切り上げ
    print(now_time)

if __name__ == "__main__":
    main()