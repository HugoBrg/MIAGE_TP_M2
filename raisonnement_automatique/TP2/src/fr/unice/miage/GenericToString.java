package fr.unice.miage;

import java.lang.reflect.Field;

public class GenericToString {
	
	public String toString(Object obj) throws NoSuchFieldException, SecurityException, IllegalArgumentException, IllegalAccessException {
		String ret;
		Class cl = obj.getClass();
		ret = cl.toString()+"[";
		
		for(int i=0;i<cl.getFields().length;i++) {
			String str = cl.getFields()[i].toString();
			System.out.println("Field avant : "+str);
			String[] arrOfStr = str.split(" "); 
			arrOfStr = arrOfStr[arrOfStr.length-1].split(".",arrOfStr[arrOfStr.length-1].length());
	        for (String a : arrOfStr) 
	            System.out.println(a); 
			str = arrOfStr[arrOfStr.length-1];
			System.out.println("Field après : "+str);
			ret += str+" = ";
			Field field = cl.getField(str); 
			Object fieldValue = field.get(obj);
			ret += fieldValue.toString();
			ret += "; ";
		}
		ret += "]";
		return ret;
	}
	
	public String toString(Object obj, int profondeur) throws NoSuchFieldException, SecurityException, IllegalArgumentException, IllegalAccessException {
		String ret = "";
		ret += toString(obj);
		return "";
	}
}
