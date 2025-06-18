name = "hasan"

match name:
    case "muhammad":
        print("muhammad")
    case "hasan":
        print("hasan")
    case "mehedi":
        print("mehedi")


day = 5
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
