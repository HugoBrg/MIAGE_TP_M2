package fr.unice.miage;

import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;

public class ListerSFV extends SimpleFileVisitor{
	
	public ListerSFV() {
		
	}
	
	@Override
	public FileVisitResult postVisitDirectory(Object dir, IOException exc) throws IOException {
	    System.out.println("J'ai visité : " + ((Path) dir).getFileName());
	    return FileVisitResult.CONTINUE;
	}

	@Override
	public FileVisitResult preVisitDirectory(Object dir, BasicFileAttributes attrs) throws IOException {
	    System.out.println("On va visiter: " + ((Path) dir).getFileName());
	    return FileVisitResult.CONTINUE;
	}

	@Override
	public FileVisitResult visitFile(Object file, BasicFileAttributes attrs) throws IOException {
	    System.out.println("Je visite : " + ((Path) file).getFileName());
	    return FileVisitResult.CONTINUE;
	}

	@Override
	public FileVisitResult visitFileFailed(Object file, IOException exc) throws IOException {
		// TODO Auto-generated method stub
		return super.visitFileFailed(file, exc);
	}
}
