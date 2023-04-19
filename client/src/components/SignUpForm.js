import React from "react";
import { useFormik } from "formik";
import * as yup from 'yup';

function SignUpForm({ onLogin }) {

    const validationSchema = yup.object({
        username: yup.string().required(),
        password: yup.string().required(),
        passwordConfirmation: yup
            .string()
            .oneOf([yup.ref("password"), null], "Passwords must match")
            .required(),
        address: yup.string().required(),
        img_url: yup.string().required() 
    });

    const formik = useFormik({
        initialValues: {
            username: "",
            password: "",
            passwordConfirmation: "",
            address: "",
            img_url: ""
        },
        validationSchema,
        onSubmit: (values, { setErrors, setSubmitting }) => {
          setSubmitting(true);
          fetch("/signup", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(values),
          })
            .then((r) => {
              setSubmitting(false);
              if (r.ok) {
                r.json().then((user) => onLogin(user));
              } else {
                r.json().then((err) => setErrors(err.errors));
    
              }
            })
            .catch((error) => {
              setSubmitting(false);
              console.error(error);
            });
        },
    });

    return (
        <div className='sign-up'>
            <form onSubmit={formik.handleSubmit}>
                <h2>Add New User</h2>
                <label>Username:</label>
                <input
                    className="sign-up input"
                    type='text'
                    id='username'
                    value={formik.values.username}
                    onChange={formik.handleChange}
                    placeholder='Username...'
                    />
                <label>Password:</label>
                <input
                    className='sign-up input'
                    type='password'
                    id='password'
                    value={formik.values.password}
                    onChange={formik.handleChange}
                    placeholder='password...'
                    />
                <label>Password Confirmation:</label>
                <input
                    className="sign-up input"
                    type='password'
                    id='passwordConfirmation'
                    value={formik.values.passwordConfirmation}
                    onChange={formik.handleChange}
                    placeholder='Password...'
                />
                <label>Address:</label>
                <input
                    className="sign-up input"
                    type='address'
                    id='address'
                    value={formik.values.address}
                    onChange={formik.handleChange}
                    placeholder='Address...'
                />
                <label>Bio Picture</label>
                <input
                    className="sign-up input"
                    type='img_url'
                    id='img_url'
                    value={formik.values.img_url}
                    onChange={formik.handleChange}
                    placeholder='Image URL...'
                />
                <input
                    type="submit"
                    name="submit"
                    value="signup"
                />
            </form>

        </div>
    )
}

export default SignUpForm