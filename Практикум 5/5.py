weight=int(input())
height=int(input())
weight_kg=weight*0.453592
height_m=height*0.0254
imt=round(weight_kg/(height_m**2),2)
if imt<16:
    print('выраженный дефицит массы тела')
elif 16<imt<18.5:
    print('недостаточная масса тела')
elif 18.5<=imt<25:
    print('норма')
elif 25<=imt<30:
    print('избыточная масса тела')
elif 30<=imt<35:
    print('ожирение первой степени')
elif 35<=imt<40:
    print('ожирение второй степени')
elif imt>=40:
    print('ожирение третьей степени')