import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:8181/web/index.php/auth/login')

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Username_username'), 'admin1')

WebUI.setEncryptedText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Password_password'), 
    'a627eoSpmGZbpVQxWE66kQ==')

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/button_Login'))

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/p_Admin 1'))

WebUI.verifyElementText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/p_Admin 1'), 'Admin 1')

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/a_Recruitment'))

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/button_Add'))

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Full Name_firstName'), first_name)

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Full Name_middleName'), middle_name)

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Full Name_lastName'), last_name)

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/i_-- Select --_oxd-icon bi-caret-up-fill ox_627fec'))

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Email_oxd-input oxd-input--focus'), 
    email)

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/div_Browse'))

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/input_Keywords_oxd-input oxd-input--focus'), 
    keywords)

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/i_Date of Application_oxd-icon bi-calendar _dfcec9'))

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/div_13'))

WebUI.setText(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/textarea_Notes_oxd-textarea oxd-textarea--f_0ce0e8'), 
    notes)

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/button_Save'))

WebUI.rightClick(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/div_SuccessSuccessfully Saved'))

WebUI.verifyElementPresent(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/button_Shortlist'), 0)

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/i_Recruitment_oxd-icon bi-caret-down-fill o_253719'))

WebUI.click(findTestObject('Object Repository/recruitment_candidate/Page_OrangeHRM/a_Logout'))

WebUI.closeBrowser()

