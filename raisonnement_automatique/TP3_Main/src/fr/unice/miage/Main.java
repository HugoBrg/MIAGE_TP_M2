package fr.unice.miage;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;

public class Main {
	static public void main(String[] args) throws MalformedURLException, ClassNotFoundException, NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException {
			
		URL[] url = new URL[] {new URL("file://C:\\Users\\hugob\\Desktop\\eclipse-workspace\\TP3_Test\\bin\\")};
		
		URLClassLoader ucl = new URLClassLoader(url);
		
        Class<?> classC = ucl.loadClass("fr.unice.miage.Test");
        
        Constructor<?> constructor = classC.getConstructor();
        Object objectO = constructor.newInstance();
        
        Method method = classC.getMethod("test");
        method.invoke(objectO);
	}
}
