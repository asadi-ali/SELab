package usermanagement.service;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class UserTest {

    @Test
    public void test_user_default_constructor() {
        User testClass = new User();

        testClass.setCompanyName("cName1");
        assertEquals("cName1", testClass.getCompanyName());

        testClass.setFirstName("fName1");
        assertEquals("fName1", testClass.getFirstName());

        testClass.setLastName("lName1");
        assertEquals("lName1", testClass.getLastName());
    }
}
