#-*- coding: UTF-8 -*-
import pymysql

#将数据存入mysql中
def data_Import(sql):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='123456',db='tc',charset='utf8')
    conn.query(sql)
    conn.commit()
    conn.close()

def getData(sql):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='tc', charset='utf8')
    cursor = conn.cursor()
    data = cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data, result
if __name__=='__main__':
    try:
        filename = 'yancheng_train_20171226'
        with open('data/' + filename + '.csv', 'r') as f:
            cvs_data = f.readlines()
            Xname = cvs_data[0]
            Xname_list = Xname.strip().split(',')
            for k in xrange(len(cvs_data)):
                if k >= 1:
                    name = cvs_data[k]
                    data = name.strip().split(',')
                    sql = "insert into info(sale_date,class_id,sale_quantity,brand_id,compartment,type_id,level_id,department_id,TR,gearbox_type,displacement,if_charging,price_level,price,driven_type_id,fuel_type_id,newenergy_type_id,emission_standards_id,if_MPV_id,if_luxurious_id,power,cylinder_number,engine_torque,car_length,car_width,car_height,total_quality,equipment_quality,rated_passenger,wheelbase,front_track,rear_track) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18],data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27],data[28], data[29], data[30], data[31])
                    data_Import(sql)
            print("数据已存入数据库")
    except Exception as e:
        print(str(e))
        print("任务完成")