import streamlit as st
from dotenv import load_dotenv

import ice_breaker
from output_parsers.linkedin_profile_output_parser import LinkedInProfileOutputParser

if __name__ == "__main__":
    load_dotenv()
    st.header("LinkedIn Profile Information...")

    # get text from user
    input_text = st.text_input("Type to generate LinkedIn profile information...")

    if input_text:

        try:
            # generate LinkedIn profile information
            profile_information: LinkedInProfileOutputParser = ice_breaker.generate_linkedin_profile_information(
                user_text=input_text)

            # check if the profile information is not None
            # and display the information
            if profile_information is not None:
                st.success("LinkedIn profile information generated successfully.")

                st.subheader("Public LinkedIn Profile URL")
                st.write(profile_information.profile_url)

                st.subheader("Public Profile Picture")
                if profile_information.profile_picture_url:
                    st.image(profile_information.profile_picture_url)
                else:
                    st.warning("No public profile picture available.")

                st.subheader("Name")
                st.write(profile_information.name)

                st.subheader("Location")
                st.write(profile_information.location)

                st.subheader("Current Job")
                st.write(profile_information.current_job)

                st.subheader("Current Company")
                st.write(profile_information.current_company)

                st.subheader("Short Summary")
                st.write(profile_information.short_summary)

                st.subheader("Two Interesting Facts")
                if profile_information.facts:
                    for fact in profile_information.facts:
                        st.write(f"- {fact}")
                else:
                    st.warning("No interesting facts available.")

                st.subheader("Two Core Skills")
                if profile_information.skills:
                    for skill in profile_information.skills:
                        st.write(f"- {skill}")
                else:
                    st.warning("No core skills available.")

                st.subheader("Two Companies with overall years experience")
                if profile_information.experience:
                    for experience in profile_information.experience:
                        st.write(f"- {experience}")
                else:
                    st.warning("No experience available.")

                st.subheader("Two Certifications")
                if profile_information.certifications:
                    for certification in profile_information.certifications:
                        st.write(f"- {certification}")
                else:
                    st.warning("No certifications available.")
            else:
                st.error("Failed to generate LinkedIn profile information.")
        except Exception as e:
            # handle any exceptions that occur during the generation process
            st.error(f"An error occurred while generating LinkedIn profile information: {e}")
