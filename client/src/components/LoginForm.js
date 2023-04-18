import React from  "react";
import { useFormik } from 'formik';
import * as yup from "yup";

function LoginForm({onLogin}) {

    const validationSchema = yup.object({
        username: yup.string().required(),
        password: yup.string().required(),
    });

    const formik = useFormik({
        initialValues: {
          username: "",
          password: "",
        },
        
        validationSchema,
        onSubmit: (values, { setErrors, setSubmitting }) => {
            setSubmitting(true);
            fetch("/login", {
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
                console.log(`Error: ${error}`)
            });
        },
    });


    return (
        <form onSubmit={formik.handleSubmit}>
            <input
                type="text"
                id="username"
                value={formik.values.username}
                onChange={formik.handleChange}
            />
            <input
                type="password"
                id="password"
                value={formik.values.password} 
                onChange={formik.handleChange}
            />
            <input
                type="submit"
                name="submit"
                value="Login"
            />
        </form>
    )
}

export default LoginForm;