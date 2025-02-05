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
----------------------------------------------*****------------------------------------

Extent Report 3 Example

package com.hematite.test;

import java.io.File;
import java.io.IOException;
import java.util.Calendar;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.testng.ISuite;
import org.testng.ISuiteListener;
import org.testng.ITestListener;
import org.testng.ITestResult;
import org.testng.annotations.Listeners;

import com.relevantcodes.extentreports.ExtentReports;
import com.relevantcodes.extentreports.ExtentTest;
import com.relevantcodes.extentreports.LogStatus;


@Listeners(com.hematite.test.QuizAppExtentReportDetails.class)
public class QuizAppExtentReportDetails extends SignUpTest1 implements ITestListener, ISuiteListener  {

	public static ExtentReports report;
	public static ExtentTest logger;
	public void onStart(ISuite suite) {
		//Create an html report for the suite that is executed
	   report = new ExtentReports(System.getProperty("user.dir") + "/reports/FinalReport.html");
	}

	
	public void onFinish(ISuite suite) {
		report.flush();
	}

	
	public void onTestStart(ITestResult result) {
		logger = report.startTest(result.getMethod().getMethodName());
		logger.log(LogStatus.INFO, "Executing test: " + result.getMethod().getMethodName());

	}

	
	public void onTestSuccess(ITestResult result) {
		logger.log(LogStatus.INFO, "Finished executing test");
	}

	
	public void onTestFailure(ITestResult result) {
		
		WebDriver driver = (WebDriver) result.getTestContext().getAttribute("WebDriver");
	    if (driver != null) {
	        String fileName = String.format("Screenshot-%s.png", Calendar.getInstance().getTimeInMillis());
	        File srcFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
	        File destFile = new File("./screenshots/" + fileName);
	        try {
	            FileUtils.copyFile(srcFile, destFile);
	            System.out.println("Screenshot taken, saved in screenshots folder");
	            logger.log(LogStatus.FAIL, "Test failed, screenshot saved: " + destFile.getAbsolutePath());
	        } catch (IOException e) {
	            System.out.println("Failed to save screenshot");
	            logger.log(LogStatus.FAIL, "Failed to save screenshot");
	        }
	    } else {
	        System.out.println("Driver is null, cannot take screenshot");
	        logger.log(LogStatus.FAIL, "Driver is null, screenshot not taken");
	    }
			
	}

	
	public void onTestSkipped(ITestResult result) {
		logger.log(LogStatus.SKIP, "Test skipped");
	}
	

}







---------------------------*****-------------------------------------------
Required dependencies

<dependencies>
  
  <!-- https://mvnrepository.com/artifact/org.apache.poi/poi -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.5</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.5</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>3.0.0-beta2</version>
</dependency>

<!-- https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-api -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>3.0.0-beta2</version>
</dependency>

	  <!-- pom.xml -->
<dependency>
    <groupId>com.aventstack</groupId>
    <artifactId>extentreports</artifactId>
    <version>5.1.1</version>
</dependency>

<!--Added new dependencies -->
	 		
		<!-- SLF4j bridge to prevent slfj error message -->
		<dependency>
			<groupId>org.apache.logging.log4j</groupId>
			<artifactId>log4j-slf4j-impl</artifactId>
			<version>2.11.2</version>
		</dependency>

		<!-- https://mvnrepository.com/artifact/com.relevantcodes/extentreports -->
		<dependency>
			<groupId>com.relevantcodes</groupId>
			<artifactId>extentreports</artifactId>
			<version>2.41.2</version>
		</dependency>

		<!-- https://mvnrepository.com/artifact/commons-io/commons-io -->
		<dependency>
			<groupId>commons-io</groupId>
			<artifactId>commons-io</artifactId>
			<version>2.5</version>
		</dependency>


<!-- End Of dependencies-->

<!-- https://mvnrepository.com/artifact/org.testng/testng -->
<dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>7.10.2</version>
    <scope>test</scope>
</dependency>
  
 
    <dependency>
 -----------------------------------------------------------------******------------------------------------------------------------------------

 MyListernes class

 package com.hematite.test;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;


public class MyListerners implements ITestListener{

	WebDriver driver = new ChromeDriver();
	
	public void onStart(ITestContext context) {
		// TODO Auto-generated method stub
		
		System.out.println("Testcases started");
		
	}
	
	@Override
	public void onTestStart(ITestResult result) {
		// TODO Auto-generated method stub
		
		System.out.println("Testcases executed");
	}
	
	@Override
	public void onTestSuccess(ITestResult result) {
		// TODO Auto-generated method stub
		
		System.out.println("Success");
		
			}
	
	@Override
	public void onTestFailure(ITestResult result) {
		// TODO Auto-generated method stub
		
		System.out.println("Failed");
		
	}
	
	@Override
	public void onTestSkipped(ITestResult result) {
		// TODO Auto-generated method stub
		
		System.out.println("Skipped");
		
	}
	
	
	@Override
	public void onFinish(ITestContext context) {
		// TODO Auto-generated method stub
		
		
		
	}
	
	
}



    
