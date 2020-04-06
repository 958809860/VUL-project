
#!python  
import os,sys,plistlib
from xml.etree import ElementTree  
from PIL import Image  
  
def tree_to_dict(tree):  
    d = {}  
    for index, item in enumerate(tree):  
        if item.tag == 'key':  
            if tree[index+1].tag == 'string':  
                d[item.text] = tree[index + 1].text  
            elif tree[index + 1].tag == 'true':  
                d[item.text] = True  
            elif tree[index + 1].tag == 'false':  
                d[item.text] = False  
            elif tree[index+1].tag == 'dict':  
                d[item.text] = tree_to_dict(tree[index+1])  
    return d  
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False

def gen_png_from_plist(plist_filename, png_filename):  
    file_path = plist_filename.replace('.plist', '')  
    big_image = Image.open(png_filename)  
    root = ElementTree.fromstring(open(plist_filename, 'r',encoding='UTF-8').read())  
    plist_dict = tree_to_dict(root[0])  
    to_list = lambda x: x.replace('{','').replace('}','').split(',')  
    for k,v in plist_dict['frames'].items():  
        print('v:',v)
        rectlist = to_list(v['frame'])  
        width = int( rectlist[3] if v['rotated'] else rectlist[2] )  
        height = int( rectlist[2] if v['rotated'] else rectlist[3] )  
        box=(   
            int(rectlist[0]),  
            int(rectlist[1]),  
            int(rectlist[0]) + width,  
            int(rectlist[1]) + height,  
            )  
        sizelist = [ int(x) for x in to_list(v['sourceSize'])]  
        rect_on_big = big_image.crop(box)  
  
        if v['rotated']:  
            #rect_on_big = rect_on_big.rotate(90)  
            rect_on_big=rect_on_big.transpose(Image.ROTATE_90)
  
        result_image = Image.new('RGBA', sizelist, (0,0,0,0))  
        if v['rotated']:  
            result_box=(  
                ( sizelist[0] - height )//2,  
                ( sizelist[1] - width )//2,  
                ( sizelist[0] + height )//2,  
                ( sizelist[1] + width )//2  
                )  
        else:  
            result_box=(  
                ( sizelist[0] - width )//2,  
                ( sizelist[1] - height )//2,  
                ( sizelist[0] + width )//2,  
                ( sizelist[1] + height )//2  
                )  
        print('rect_on_big:',rect_on_big,'result_box:',result_box)
        result_image.paste(rect_on_big, result_box, mask=0)
        #mkdir(save_path+'/' +file_path+'/' + k.split("/"+k.split("/")[-1])[0])
        #outfile = (save_path+'/'+file_path+'/' + k).replace('gift_', '')
        mkdir(save_path+'/' + plist_filename.split(".plist")[0])
        outfile = (save_path+'/' + plist_filename.split(".plist")[0] + "/" + k.split("/")[-1])
        print("outfile",outfile)
        print(outfile,"generated")
        result_image.save(outfile)  
  
if __name__ == '__main__':     
    a = sys.argv[1].replace(" ","")
    b = sys.argv[2].replace(" ","")
    print(a+"\n" + b)
    #filename = sys.argv[1] 
    #filename =  'mahjongs'
    
    #直接使用
    #plist_filename = filename + '.plist'  
    #png_filename = filename + '.png'  
    
    #調用
    save_path = a.split("/"+a.split("/")[-1])[0]
    os.chdir(save_path)
    plist_filename = a.split("/")[-1]
    png_filename = b.split("/")[-1]
    if (os.path.exists(a) and os.path.exists(b)):  
        gen_png_from_plist( plist_filename, png_filename )  
    else: 
        print("make sure you have boith plist and png files in the same directory") 
