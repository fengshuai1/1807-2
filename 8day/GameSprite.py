#coding=utf-8
import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)#常量
FRAME_PER_SEC = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT #pygame常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1 #pygame常量
#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy0_down1.png')
bg2 = pygame.image.load('./images/enemy0_down2.png')
bg3 = pygame.image.load('./images/enemy0_down3.png')
bg4 = pygame.image.load('./images/enemy0_down4.png')
 
#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()
 
#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):#父类 大写

    def __init__(self,image,speed=1):
        super(GameSprite,self).__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y +=self.speed
#背景精灵
class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		imagename = './images/bg.png'
		super(BackGroundSprite,self).__init__(imagename)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super(BackGroundSprite,self).update()#调用父类
		#把移除屏幕的背景放到屏幕上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height	
class Enemy(GameSprite): #敌机精灵

	def __init__(self):
		imagename = './images/plane.png'

		#调用父类方法，创建敌机精灵，并且制定敌机的图像
		super(Enemy,self).__init__(imagename)
		self.speed = random.randint(1,5)#设置敌机随机速度
		max = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max)#随机位置
		self.rect.bottom = 0#平滑出现
		self.down_index = 0#敌机销毁图片
	
	def update(self):
		#调用父类方法，让敌机在垂直方向运动
		super(Enemy,self).update()
		#判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
		if self.rect.y >= SCREEN_RECT.height:#销毁敌机
			#print("敌机飞出屏幕...")
			self.kill()

class HeroSprite(GameSprite): #英雄精灵
	def __init__(self):
		imagename ='./images/hero1.png'
		super(HeroSprite,self).__init__(imagename,0)
		self.bullet_group = pygame.sprite.Group()#创建子弹精灵组
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.height - 60

	def update(self):
		# super().update() 
		self.rect.x += self.speed
		self.rect.y += self.speed1  
			
		if self.rect.left <= 0:
			self.rect.left = 0

		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width
		elif self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
	
	def fire(self):
		bullet = BulletSprite()
		bullet.rect.x = self.rect.centerx
		bullet.rect.bottom = self.rect.top 

		bullet1 = BulletSprite()
		bullet1.rect.x = self.rect.centerx-35
		bullet1.rect.bottom = self.rect.top+30 

		bullet2 = BulletSprite()
		bullet2.rect.x = self.rect.centerx+35
		bullet2.rect.bottom = self.rect.top+30 
		self.bullet_group.add(bullet1)
		self.bullet_group.add(bullet2)
		self.bullet_group.add(bullet)
		     

    

#子弹精灵
class BulletSprite(GameSprite):
    def __init__(self):
        imagename = "./images/bullet-3.gif"
        super(BulletSprite,self).__init__(imagename,-10)

    def update(self):
        super(BulletSprite,self).update() 
	
        
        #子弹飞出屏幕 要销毁
        if self.rect.bottom <= 0:
           self.kill()                   
