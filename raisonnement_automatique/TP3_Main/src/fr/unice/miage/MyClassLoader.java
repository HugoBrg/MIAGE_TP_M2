package fr.unice.miage;

import java.io.File;
import java.security.SecureClassLoader;
import java.util.ArrayList;

public class MyClassLoader extends SecureClassLoader {  
    
	private ArrayList<File> path = null;  
    
    public MyClassLoader(ArrayList<File> p) {  
      this.path = p;  
    }
    
    @Override  
    protected Class<?> findClass(String name) throws ClassNotFoundException {  
      byte[] b = loadClassData(name);  
      return super.defineClass(name, b, 0, b.length);  
    }  
      
    private byte[] loadClassData(String name) throws ClassNotFoundException {  
    // TODO  A COMPLETER    
     return null;  
    }  

   private void rechercheProfondeur(File file) {
	   System.out.println("X");
		File[] listFile = file.listFiles();
		System.out.println("X");
    	for(int x=0;x<listFile.length;x++) {
    		this.path.add(listFile[x]);
    	}
    	System.out.println("X");
    	for(int i=0;i<listFile.length;i++) {
			if(listFile[i].isDirectory()) {
				MyClassLoader mcl = new MyClassLoader(this.path);
				mcl.rechercheProfondeur(listFile[i]);
				System.out.println(listFile[i]);
			}
			else if(listFile[i].isFile()) {
				System.out.println(listFile[i]);
			}			
		}
    }
    
    
    @Override
    public Class<?> loadClass(String name){
    	File file = new File(this.path.get(0).getAbsolutePath());
    	System.out.println(this.path.get(0).getAbsolutePath());
    	rechercheProfondeur(file);
		return null;
    	 
     }
    public static void main(String[] args) {  
      ArrayList<File> al = new ArrayList<File>();  
      //al.add(new File(....));  
      al.add(new File("file://C:\\Users\\hugob\\Desktop\\eclipse-workspace\\"));
     MyClassLoader myCL = new MyClassLoader(al);  
     myCL.loadClass("fr.unice.miage");
     }  
   }  