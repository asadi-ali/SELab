package usermanagement.service;

import org.junit.Test;
import usermanagement.entity.Person;

import static org.junit.Assert.assertEquals;

public class TransformServiceTest {

    @Test
    public void test_to_user_domain() {
        Person person = new Person();
        TransformService testClass = new TransformService();

        person.setfName("fName");
        person.setlName("lName");
        person.setCompanyName("cName");
        person.setPersonId(123);

        User user = testClass.toUserDomain(person);
        assertEquals("fName", user.getFirstName());
        assertEquals("lName", user.getLastName());
        assertEquals("cName", user.getCompanyName());
        assertEquals(Integer.valueOf(123), user.getUserId());
    }
}
