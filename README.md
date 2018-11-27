### 1. Diango入门

1. 在项目的models中定义模型类  模型类继承自modes.Model 
  不需要创建主键列  在生成时会自动添加 并且值为自动增长
  
2. 激活模型  在setting.py文件中 将你的项目加入到installed_apps代码块中   
 使用pycharm创建的项目 不必加入  使用django版本**大于2**时 在关联外键时写<label style="color:blue"> 
 models.ForeignKey("ShopInfo", on_delete=models.CASCADE, )</label>
 
3. 管理界面本地化   
    ```编辑settings.py文件，设置编码、时区```  
    ```LANGUAGE_CODE = 'zh-Hans'  TIME_ZONE = 'Asia/Shanghai' ```  
4. 生成迁移文件  
    >  ```python manage.py makemigrations ```  
      ```python manage.py migrate   ```  
      
5. 管理站点--创建管理员账户    
   >```python manage.py createsuperuser，按提示输入用户名、邮箱、密码```  
6. 向admin中注册models中的模型  
   >             ```请查看demo  ```
    
7. 视图  
     >  视图对web请求进行回应 <br> 视图就是一个Python函数，被定义在views.py中  
   
      1. 在配置文件urls.py中加入项目中定义的urls.py文件
      2. 在views.py中新建请求解析渲染  
           ```python
         def index(request):
                shopList = ShopInfo.objects.all();
                context = {"list": shopList}
                return render(request, "shoptest/index.html", context)
            ``` 
## 2.Diango 模型
    
       
            
            
        

   
    
   
     
    
        
  