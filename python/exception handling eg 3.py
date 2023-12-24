try:
    a=int(input())
    b=int(input())
except ValueError as e:
    print("value Error",e)
except typeError as e:
    print("type Error",e)
finally:
    print("done")
