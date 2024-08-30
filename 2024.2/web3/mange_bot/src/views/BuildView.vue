<script setup lang="ts">
    import PartSelector from '@/components/PartSelector.vue';
import type { ItemCart } from '@/models/cart';
    import { Part, PartsResponse } from '@/models/part';
    import { getParts } from '@Services/part.service';
    import { ref, reactive, type Ref } from 'vue';
    import DotLoader from 'vue-spinner/src/DotLoader.vue';

    const availableParts: Ref<PartsResponse> = ref(new PartsResponse());
  
    // const selectedHead: Ref<Part | null> = ref(null);
    // const selectedLeftArm: Ref<Part | null> = ref(null);
    // const selectedRightArm: Ref<Part | null> = ref(null);
    // const selectedTorso: Ref<Part | null> = ref(null);
    // const selectedBase: Ref<Part | null> = ref(null);

    const selectedParts = reactive<ItemCart>({
        head: new Part(),
        leftArm: new Part(),
        rightArm: new Part(),
        base: new Part(),
        torso: new Part()
    })

    getParts()
    .then((parts) => {
        availableParts.value = parts;

        selectedParts.head = parts.heads[0] ?? null;
        selectedParts.leftArm = parts.arms[0] ?? null;
        selectedParts.rightArm = parts.arms[0] ?? null;
        selectedParts.torso = parts.torsos[0] ?? null;
        selectedParts.base = parts.bases[0] ?? null;
    })
    .catch((error) => console.error(error));

    const addCart = ()=> {
        console.log(selectedParts)
    } 
</script>

<template>
    <div v-if="availableParts.arms.length > 0">
        <section class="top-row">
            <PartSelector
                :parts="availableParts.heads"
                position="top"
                v-model="selectedParts.head"          
            />
        </section>
        <section class="middle-row">
            <PartSelector
                :parts="availableParts.arms"
                position="left"
                v-model="selectedParts.leftArm"
            />
            <PartSelector
                :parts="availableParts.torsos"
                position="center"
                v-model="selectedParts.torso"
            />
            <PartSelector
                :parts="availableParts.arms"
                position="right"
                v-model="selectedParts.rightArm"  
            />
        </section>
        <section class="bottom-row">
            <PartSelector
                :parts="availableParts.bases"
                position="bottom"
                v-model="selectedParts.base"
            />
        </section>   
        
        <div class="flex flex-row align-items-center justify-content-center">
            <button @click="addCart" id="add-cart" class="mt-5 app-dark-button">
                {{ $t('build.add_cart') }}
            </button>
        </div>
    </div>
    <div class="loader" v-else>
        <DotLoader />
    </div>
      
</template>

<style scoped lang="scss">

    #add-cart{
        padding: 0.5rem 1rem;
    }
    
    .loader {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 70%;
    }

    .top-row{
        display: flex;
        justify-content: space-around;
    }

    .middle-row{
        display: flex;
        justify-content: center;
    }

    .bottom-row{
        display: flex;
        justify-content: space-around;
    }
</style>