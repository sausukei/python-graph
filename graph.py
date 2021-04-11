import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

if __name__ == '__main__':
   
    x = 1
    y = 1
    cnt = 0
    points = []
    result = {}
    while x == 1:
        while y == 1:
            point = float(input('得られた数値を代入:'))
            points.append(point)
            y = int(input('計測をやめる→0, やめない→1, 入力ミス→2:'))
            while y == 2:
                point = float(input('得られた数値を代入:'))
                points[cnt] = point 
                y = int(input('計測をやめる→0, やめない→1, 入力ミス→2:'))
                
            cnt += 1
        deta_name = input('このデータの名前は?:')
        deta_symbol = input('このデータの記号は?:')
        deta_unit = input('このデータの単位は?:')
        result[deta_name+' '+deta_symbol+'['+deta_unit+']'] = points
        x = int(input('測定完了→0, 続行→1 変更→2:'))
        if x == 1:
            y = 1
        while x == 2:
            delete_name = deta_name+' '+deta_symbol+'['+deta_unit+']'
            deta_name = input('このデータの名前は?:')
            deta_symbol = input('このデータの記号は?:')
            deta_unit = input('このデータの単位は?:')
            result[deta_name+' '+deta_symbol+'['+deta_unit+']'] = result.pop(delete_name)
            x = int(input('測定完了→0, 続行→1 変更→2:'))
            deta_name = delete_name

        


        print(result)
    
    df = pd.DataFrame(result)
    print(pd.DataFrame([result]))
    fig, ax = plt.subplots(figsize=(3,3))

    ax.axis('off')
    ax.axis('tight')

    ax.table(cellText=df.values,
	colLabels=df.columns,
	bbox=[0, 0, 1, 1],
	)

    plt.show()

    '''
    height = input('縦軸は?')
    width = input('横軸は?')
 
    height = result[height]
    width = result[width]
    # 散布図を描画
    plt.scatter(height, width)
    '''

    
    
