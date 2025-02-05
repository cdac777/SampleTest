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

Extent Report Example 1

package com.hematite.test;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.aventstack.extentreports.reporter.configuration.Theme;

public class QuizAppExtentReport implements ITestListener {

    public ExtentSparkReporter sparkReporter;
    public ExtentReports extent;
    public ExtentTest test;
    private WebDriver driver;

    @Override
    public void onStart(ITestContext context) {
        sparkReporter = new ExtentSparkReporter(System.getProperty("user.dir") + "/reports/QuizAppReport.html");

        sparkReporter.config().setDocumentTitle("Hematite QuizApp Report");
        sparkReporter.config().setReportName("Function Testing Of SignUp & Login Page");
        sparkReporter.config().setTheme(Theme.DARK);

        extent = new ExtentReports();
        extent.attachReporter(sparkReporter);

        extent.setSystemInfo("QuizAppURL", "http://quiz.hematitecorp.com/");
        extent.setSystemInfo("Environment", "SQA");
        extent.setSystemInfo("Tester Name", "Monica Fulare");
        extent.setSystemInfo("OS", "Windows-11");
        extent.setSystemInfo("BrowserName", "Chrome");
    }

    @Override
    public void onTestSuccess(ITestResult result) {
        test = extent.createTest(result.getName());
        test.log(Status.PASS, "TestCase Passed: " + result.getName());
    }

    @Override
    public void onTestFailure(ITestResult result) {
        test = extent.createTest(result.getName());
        test.log(Status.FAIL, "TestCase Failed: " + result.getName());
        test.log(Status.FAIL, "Error: " + result.getThrowable());

        // Capture and attach screenshot
        if (driver != null) {
            String screenshotPath = captureScreenshot(result.getName());
            if (screenshotPath != null) {
                try {
                    test.addScreenCaptureFromPath(screenshotPath, "Failure Screenshot");
                } catch (Exception e) {
                    test.log(Status.FAIL, "Failed to attach screenshot: " + e.getMessage());
                }
            }
        }
    }

    @Override
    public void onTestSkipped(ITestResult result) {
        test = extent.createTest(result.getName());
        test.log(Status.SKIP, "TestCase Skipped: " + result.getName());
        test.log(Status.SKIP, "Reason: " + result.getThrowable());
    }

    @Override
    public void onFinish(ITestContext context) {
        extent.flush();
    }

    // Utility method to capture a screenshot
    private String captureScreenshot(String testName) {
        String screenshotDirectoryPath = System.getProperty("user.dir") + "/reports/screenshots/";
        String screenshotPath = screenshotDirectoryPath + testName + ".png";
        File screenshotFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);

        try {
            File screenshotDir = new File(screenshotDirectoryPath);
            if (!screenshotDir.exists()) {
                boolean isDirCreated = screenshotDir.mkdirs();
                if (!isDirCreated) {
                    System.err.println("Failed to create screenshots directory: " + screenshotDirectoryPath);
                    return null;
                }
            }

            File destinationFile = new File(screenshotPath);
            Files.copy(screenshotFile.toPath(), destinationFile.toPath());
            return screenshotPath;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    // Setter method to pass WebDriver instance (should be called in your test class)
    public void setDriver(WebDriver driver) {
        this.driver = driver;
    }
}

-------------------------------------------------*****-------------------------------------------------------------------------------
Extent Report Example 2

package com.hematite.test;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.aventstack.extentreports.reporter.configuration.Theme;

public class QuizAppExtentReport implements ITestListener {

    public ExtentSparkReporter sparkReporter;
    public ExtentReports extent;
    public ExtentTest test;
    private WebDriver driver;

    @Override
    public void onStart(ITestContext context) {
        sparkReporter = new ExtentSparkReporter(System.getProperty("user.dir") + "/reports/QuizAppReport.html");

        sparkReporter.config().setDocumentTitle("Hematite QuizApp Report");
        sparkReporter.config().setReportName("Function Testing Of SignUp & Login Page");
        sparkReporter.config().setTheme(Theme.DARK);

        extent = new ExtentReports();
        extent.attachReporter(sparkReporter);

        extent.setSystemInfo("QuizAppURL", "http://quiz.hematitecorp.com/");
        extent.setSystemInfo("Environment", "SQA");
        extent.setSystemInfo("Tester Name", "Monica Fulare");
        extent.setSystemInfo("OS", "Windows-11");
        extent.setSystemInfo("BrowserName", "Chrome");
    }

    @Override
    public void onTestSuccess(ITestResult result) {
        test = extent.createTest(result.getName());
        test.log(Status.PASS, "TestCase Passed: " + result.getName());
    }

    @Override
    public void onTestFailure(ITestResult result) {
        test = extent.createTest(result.getName());
        test.log(Status.FAIL, "TestCase Failed: " + result.getName());
        test.log(Status.FAIL, "Error: " + result.getThrowable());

        // Capture and attach screenshot
        if (driver != null) {
            String screenshotPath = captureScreenshot(result.getName());
            if (screenshotPath != null) {
                try {
                    test.addScreenCaptureFromPath(screenshotPath, "Failure Screenshot");
                } catch (Exception e) {
                    test.log(Status.FAIL, "Failed to attach screenshot: " + e.getMessage());
                }
            }
        }
    }

    @Override
    public void onTestSkipped(ITestResult result) {
        test = extent.createTest(result.getName());
        test.log(Status.SKIP, "TestCase Skipped: " + result.getName());
        test.log(Status.SKIP, "Reason: " + result.getThrowable());
    }

    @Override
    public void onFinish(ITestContext context) {
        extent.flush();
    }

    // Utility method to capture a screenshot
    private String captureScreenshot(String testName) {
        String screenshotDirectoryPath = System.getProperty("user.dir") + "/reports/screenshots/";
        String screenshotPath = screenshotDirectoryPath + testName + ".png";
        File screenshotFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);

        try {
            File screenshotDir = new File(screenshotDirectoryPath);
            if (!screenshotDir.exists()) {
                boolean isDirCreated = screenshotDir.mkdirs();
                if (!isDirCreated) {
                    System.err.println("Failed to create screenshots directory: " + screenshotDirectoryPath);
                    return null;
                }
            }

            File destinationFile = new File(screenshotPath);
            Files.copy(screenshotFile.toPath(), destinationFile.toPath());
            return screenshotPath;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    // Setter method to pass WebDriver instance (should be called in your test class)
    public void setDriver(WebDriver driver) {
        this.driver = driver;
    }
}

-------------
