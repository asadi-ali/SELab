package usermanagement.exception;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class UserNotFoundExceptionTest {

    @Test
    public void test_person_default_constructor() {
        UserNotFoundException testClass = new UserNotFoundException("message", 123);
        assertEquals(Integer.valueOf(123), testClass.getUserId());
    }
}
