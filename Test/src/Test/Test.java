package Test;    //声明该类所在的包为Test,package为包的关键字
import java.util.Date;    //导入java.util包中的 Date类，用来封装当前的日期和时间

public class Test {    //声明一个名为Test的public类
	
	static String str1 = "你好,";    //在Test类中声明并赋值一个名为str1的全局变量（成员变量）

	public static void main(String[] args) {
		String str2 = "Java!";    //在main()方法中声明并赋值一个名为str2的局部变量
		System.out.println(str1);    //打印字符串
		System.out.println(str2);
		System.out.println(str1 + str2);
	    Date nowtime = new Date();    //初始化Date对象
	    System.out.println("当前时间："+nowtime.toString());    //使用 toString() 函数显示日期时间
	}

}


//#### 包声明
//通过package关键字声明包

//#### 导入API类库
//通过import关键字导入相关的类.

//#### 主方法
//main()方法是类体中的主方法。该方法从“{”号开始，至“}”号结束。main()方法是程序开始执行的位置。
//main()方法必须声明为"public static void"，它们分别是main()方法的权限修饰符、静态修饰符和返回值修饰符。
//"String[] args"是一个字符串类型的数组，是main()方法的参数。

//#### 变量
//全局变量（成员变量）声明在类中，是类的属性。
//局部变量声明在方法中，是方法的属性。