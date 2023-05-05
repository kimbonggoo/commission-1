from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from parsed_data.models import TapbitData
from accounts.models import User
import heapq

@login_required
def main(request):
    my = request.user
    lower_uids = my.lower_uids.split(',')

    try:
        my_data = TapbitData.objects.get(uid=my.uid)
    except:
        pass
    
    # 하부 계정 개수
    lower_count = 0
    if '' in lower_uids:
        pass
    else:
        lower_count = len(lower_uids)

    # 하부 리베이트
    lower_rebate = 0
    try:
        for l_uid in lower_uids:
            l_data = TapbitData.objects.get(uid=l_uid)
            lower_rebate += int(l_data.upper_rebate)
    except:
        pass

    # 총 리베이트
    total_rebate = 0
    try:
        total_rebate = int(my_data.rebate) + lower_rebate
    except:
        pass

    # 인출 가능 금액
    withdrawal = int(total_rebate) - int(my.use_rebate)

    # 랭킹 순위 찾기
    top_ranks = all_rebate()
    top_ranks.sort(reverse=True)

    context = {
        'uid': my.uid,
        'lower_count': lower_count,
        "total_rebate": total_rebate,
        'withdrawal': withdrawal,
        'top_ranks': top_ranks,
    }
    return render(request, 'views/index.html', context)

def all_rebate():
    all_user = User.objects.all()
    top_ranks = []

    for user in all_user:
        if user.username == 'qudwls':
            continue
        
        try:
            lower_uids = user.lower_uids.split(',')
            data = TapbitData.objects.get(uid=user.uid)

            # 하부 리베이트
            lower_rebate = 0
            try:
                for l_uid in lower_uids:
                    l_data = TapbitData.objects.get(uid=l_uid)
                    lower_rebate += int(l_data.upper_rebate)
            except:
                pass

            # 총 유저 리베이트
            user_rebate = int(data.rebate) + lower_rebate

            if len(top_ranks) < 3:
                heapq.heappush(top_ranks, (user_rebate, user.uid))
            else:
                if  top_ranks[0][0] < user_rebate:
                    heapq.heappop(top_ranks)
                    heapq.heappush(top_ranks, (user_rebate, user.uid))
        except:
            pass

    return top_ranks
