from django.contrib.auth import get_user_model

User = get_user_model()

_user = User.objects.get(username = "balanceuser")

def bubble_sort_like(arr):
    arr2=arr
    n = len(arr2)

    # change_index_likes = []
    # change_index_dislikes = []

    # for i in arr2:
    #     if i.likes.count() == 0:
    #         i.likes.add(_user)
    #         print(i.id)
    #         change_index_likes.append(i.id)
    #     if i.dislikes.count() == 0:
    #         i.dislikes.add(_user)
    #         print(i.id)
    #         change_index_dislikes.append(i.id)
        
    for i in range(n):
        for j in range(0, n-i-1):
            if arr2[j].likes.count()/arr2[j].dislikes.count() < arr2[j+1].likes.count()/arr2[j+1].dislikes.count():
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

    # if len(change_index_likes):
    #     for i in change_index_likes:
    #         print(i)
    #         arr2[i].likes.remove(_user)

    # if len(change_index_dislikes):
    #     for i in change_index_dislikes:
    #         print(i)
    #         arr2[i].dislikes.remove(_user)

    return arr2


def get_top_post(arr):
    arr2 = arr
    n = len(arr2)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr2[j].views.count() < arr2[j+1].views.count():
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

    return arr2[0]  
