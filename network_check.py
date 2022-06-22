class IP_check(object):
    def make_ip(self,ip):
        """
        输入一个ip地址，将对应的ip地址转化为一个32位的二进制
        """
        ipbin=''
        ip_A=str(ip).split(".")
        for i in  ip_A:
            A=bin(int(i))
            ip_a=A[2:]#字符串除去前面的0b进行
            #print(ip_a)
            while len(str(ip_a))<8:
                #保证每一位都为8位
                a='0'
                ip_a=a+ip_a
            ipbin+=ip_a
        return ipbin
    def make_mask(self,mask):
        """
        输入一个1-32的整数或者类似于255.255.255.0的掩码，返回一个32位的2进制序列
        """
        if len(mask)<=2:
            make_list = []
            for i in range(32):
                #创建一个32全是0的空列表，输入的整数含有多少1，就在列表变为多少1
                make_list.append(0)
            for i in range(0,int(mask)):
                make_list[i]=1
            make_list=str(make_list)
            print(make_list)
            make_deal=(make_list.replace(", ",""))[1:-1]
        elif 32>=len(mask)!=1:
            make_deal=self.make_ip(mask)
        return make_deal
    def ip_check(self,ip,network):
        """
        输入一个ip，输入一个类似2.1.1.1/32的网络段，判断ip是否在这个网段内
        """
        make_network=network.split("/")
        network_ip=int(self.make_ip(make_network[0]),2)
        network_mask=int(self.make_mask(make_network[1]),2)
        Ip = int(self.make_ip(ip),2)
        #转为int数字，自动会将字符串前面的0去掉，导致保留位不到32，int(xx,2)表示一个字符串只存在0,1转化为10进制
        if network_ip & network_mask == Ip & network_mask:
            print("YES")
            return True
        else:
            print("NO")
            return False

if __name__ == "__main__":
    ip_1=IP_check()
    ip_1.ip_check(ip="23.2.1.1",network="23.1.1.1/255.255.0.0")
