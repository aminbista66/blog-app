def bubble_sort_like(arr):
    arr2=arr
    n = len(arr2)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr2[j].likes.count() < arr2[j+1].likes.count() :
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
    return arr2

def get_top_post(arr):
    arr2 = arr
    n = len(arr2)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr2[j].views.count() < arr2[j+1].views.count():
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

    return arr2[0]  
