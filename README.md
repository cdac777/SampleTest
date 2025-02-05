MSTest Follow the steps given in below project
https://github.com/LambdaTest/MSTest-Selenium-Sample.git
NUnit Follow the steps given in the below project
https://github.com/LambdaTest/CSharp-Selenium-Sample.git

--------------------------------------------------****----------------------------------------------------
TestNG Annotation Example

package com.hematite.testngAnnotation;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

//1.Login - pre-requisite - multipletime - @BeforeMethod = as this should execute before all methods
//2.Search - main @Test
//3.Login - pre-requisite - multipletime 
//4.Logout - pre-requisite - multipletime 
//5.Adv search - main @Test
//6.Logout - pre -requisite - multipletime - @AfterMethod = as this should execute after all methods

public class QuizAppScenario {
	
	WebDriver driver = new ChromeDriver();

	@BeforeMethod
	void loginTest() {
		System.out.println("Inside LoginStep");
		
		driver.get("http://quiz.hematitecorp.com/");
		driver.findElement(By.id("email")).sendKeys("admin@gmail.com");
		driver.findElement(By.id("password")).sendKeys("Admin@1234");
		driver.findElement(By.cssSelector("button[type='submit']")).click();
		
	}
	
	@Test //(priority = 1)
	void searchTest() throws InterruptedException {
		System.out.println("Inside SearchStep");
		
 //       Thread.sleep(1000);
//		driver.findElement(By.xpath("//span[normalize-space()='Employee']")).click();
		
		
	}
	
//	@Test(priority = 2)
//	void NewSearchTest() {
//		System.out.println("Inside NewSearchStep");
//		
//		driver.findElement(By.xpath("//input[@id=':r9:']")).sendKeys("8989898989");
//	}
	
	@AfterMethod
	void logoutTest() {
		System.out.println("Inside LogoutStep");
	
		
	}
	

}
---------------------------------------------------------------------------------*****-------------------------------------------------------
