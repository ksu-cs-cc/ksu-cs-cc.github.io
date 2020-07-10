import java.util.StringBuilder;

public class test{
	public static void main(String[] args){
		test tester = new test();
		tester.time(0); //0 is APPENDER anything else is APPENDER_LIST
		
	}

	public void time(int version){
		if(version==0){
			for(double i = 0; i <10;i++){
				double n = Math.pow(10.0,i);
				long start = System.currentTimeMillis();
				String foo = this.Appender(n,"abc");
				long end = System.currentTimeMillis();
				float sec = (end - start) / 1000F; System.out.println(sec + " seconds");
				/*
				* 10^0 0.0s
				* 10^1 0.0s
				* 10^2 0.001s
				* 10^3 0.009s 
				* 10^4 0.338s
				* 10^5 25.773s
				* 10^6 2962.513s
				* 10^7 
				* 10^8
				* 10^9
				*/
			}
		}else{
			for(double i = 0; i <10;i++){
				double n = Math.pow(10.0,i);
				long start = System.currentTimeMillis();
				String foo = this.AppenderList(n,"abc");
				long end = System.currentTimeMillis();
				float sec = (end - start) / 1000F; System.out.println(sec + " seconds");
				/*
				* 10^0 0.0s
				* 10^1 0.0s
				* 10^2 0.0s
				* 10^3 0.0s
				* 10^4 0.001s
				* 10^5 0.005s
				* 10^6 0.026s
				* 10^7 0.295s
				* 10^8 2.953s
				* 10^9 out of memory 
				*/
			}
		}
	

	}



/* ```tex
* 1. function APPENDER(NUMBER, BASE)
* 2.     RESULT = ""
* 3.     loop I from 1 to NUMBER
* 4.         RESULT = RESULT + BASE
* 5.         if I MOD 2 = 0
* 6.             RESULT = RESULT + " "
* 7.         else
* 8.             RESULT = RESULT + ", " 
* 9.     end loop
* 10.    return RESULT
* 11. end function
* ```
*/

	public void run(){
		
	}
	public String Appender(double number, String base){
		String result = "";
		for(int i = 0; i<number;i++){
			result += base;
			if(i%2==0){
				result += " ";
			}else{
				result += ", ";
			}//else
		}//for
		return(result);
	}//Appender

/* ```tex
* 1. function APPENDER_LIST(NUMBER, BASE)
* 2.     RESULT = []
* 3.     loop I from 1 to NUMBER
* 4.         RESULT.APPEND(BASE) 
* 5.         if I MOD 2 = 0
* 6.             RESULT.APPEND(" ") 
* 7.         else
* 8.             RESULT.APPEND(", ")  
* 9.     end loop
* 10.    RESULT = "".JOIN(RESULT)
* 11.    return RESULT
* 12. end function
* ```
*/
public String AppenderList(double number, String base){
	StringBuilder result = new StringBuilder();
	for(int i = 0; i<number;i++){
		result.append(base);
		if(i%2==0){
			result.append(" ");
		}else{
			result.append(", ");
		}//else
	}//for
	String sResult = result.toString();
	return(sResult);
}//AppenderList

}
