<template>
    <div>
        <input :type="type"
            :class="{ error: isError }"
            v-model="inputValue"
            :placeholder="placeholder"
            @input="sendParentValue">
        <p v-if="isError">{{ errorText }}</p>
    </div>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            default: 'text'
        },
        placeholder: {
            type: String,
            required: true
        },
        isError: {
            type: Boolean,
            default: false
        },
        errorText: {
            type: String,
            default: null
        }
    },
    model: {
        prop: 'value',
        event: 'input'
    },
    data: () => ({
        inputValue: '',
    }),
    methods: {
        sendParentValue() {
            this.$emit('input', this.inputValue)
        }
    },
}
</script>

<style>

</style>